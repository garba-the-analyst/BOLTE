#!/usr/bin/env python3
"""
HFP-X 6-DOF rigid-body simulation core (structure implementation).
===================================================================
Implements HFPX-AERO-SIX-001 (06.11 equation structure) for
HFPX-SIM-SIX-001 (19.3). See HFPX-SIM-SIX-002 for status/limits.

STATUS: UNVERIFIED — NOT in the verified-model register (19.15).
No gate decision, authority claim, or clearance may use this code
or its outputs (REQ-HFPX-ASX-004/005, MSX-005, MMV-005).

Dynamics (flat Earth, NED position, body-frame velocity):
    v_dot = F_total/m - omega x v
    omega_dot = I^-1 (M_total - omega x (I omega))
    q_dot = 0.5 * Omega(omega) * q        (unit quaternion, body<-NED)
    p_dot = C_bn(q) * v
F_total = F_aero(state) + F_prop(state, control) + F_gravity(q)
M_total = M_aero(state) + M_prop(state, control)
Force/moment callbacks are PLUG-INS (default: zero). DEMO parameters
below are ILLUSTRATIVE ONLY — not HFP-X data, not for design use.
"""

import numpy as np

G = 9.80665


def quat_normalize(q):
    return q / np.linalg.norm(q)


def quat_to_dcm(q):
    """Body<-NED direction cosine matrix from unit quaternion [w,x,y,z]."""
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y + w * z), 2 * (x * z - w * y)],
        [2 * (x * y - w * z), 1 - 2 * (x * x + z * z), 2 * (y * z + w * x)],
        [2 * (x * z + w * y), 2 * (y * z - w * x), 1 - 2 * (x * x + y * y)],
    ])


def omega_matrix(w):
    p, q, r = w
    return 0.5 * np.array([
        [0, -p, -q, -r],
        [p, 0, r, -q],
        [q, -r, 0, p],
        [r, q, -p, 0],
    ])


class SixDOF:
    """Rigid-body 6-DOF core with plug-in aero/propulsion models."""

    def __init__(self, mass, inertia, aero=None, prop=None):
        self.m = float(mass)
        self.I = np.array(inertia, dtype=float)
        self.Iinv = np.linalg.inv(self.I)
        self.aero = aero or (lambda s, u: (np.zeros(3), np.zeros(3)))
        self.prop = prop or (lambda s, u: (np.zeros(3), np.zeros(3)))

    def derivatives(self, x, u):
        """x = [pos(3 NED), vel(3 body), quat(4), rates(3 body)]."""
        p, v, q, w = x[0:3], x[3:6], quat_normalize(x[6:10]), x[10:13]
        Cbn = quat_to_dcm(q)
        Fa, Ma = self.aero(x, u)
        Fp, Mp = self.prop(x, u)
        Fg = Cbn.T @ np.array([0.0, 0.0, self.m * G])  # weight in body axes
        F = Fa + Fp + Fg
        M = Ma + Mp
        v_dot = F / self.m - np.cross(w, v)
        w_dot = self.Iinv @ (M - np.cross(w, self.I @ w))
        q_dot = omega_matrix(w) @ q
        p_dot = Cbn @ v
        return np.concatenate([p_dot, v_dot, q_dot, w_dot])

    def step_rk4(self, x, u, dt):
        k1 = self.derivatives(x, u)
        k2 = self.derivatives(x + 0.5 * dt * k1, u)
        k3 = self.derivatives(x + 0.5 * dt * k2, u)
        k4 = self.derivatives(x + dt * k3, u)
        x1 = x + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        x1[6:10] = quat_normalize(x1[6:10])
        return x1

    def simulate(self, x0, u_of_t, t_end, dt):
        n = int(round(t_end / dt)) + 1
        xs = np.zeros((n, 13))
        xs[0] = x0
        for k in range(n - 1):
            xs[k + 1] = self.step_rk4(xs[k], u_of_t(k * dt), dt)
        return np.linspace(0, t_end, n), xs


def hover_state(altitude_up_m=0.0):
    """Level-attitude rest state. NED: down positive -> altitude is -D."""
    return np.array([0.0, 0.0, -altitude_up_m,
                     0.0, 0.0, 0.0,
                     1.0, 0.0, 0.0, 0.0,
                     0.0, 0.0, 0.0])


# ------------------------------------------------------------------ demos
# DEMO PARAMETERS — ILLUSTRATIVE ONLY. Not HFP-X data. Not for design use.
DEMO = dict(mass=130.0, inertia=np.diag([12.0, 14.0, 9.0]),
            dt=0.005, note="ILLUSTRATIVE ONLY — not HFP-X data")


def _run_checks():
    from pathlib import Path
    out = Path(__file__).parent / "demo"
    out.mkdir(exist_ok=True)
    rep = []
    m, I, dt = DEMO["mass"], DEMO["inertia"], DEMO["dt"]

    # 1. Free fall: no aero/prop -> vertical accel equals g, no NaN.
    mdl = SixDOF(m, I)
    t, xs = mdl.simulate(hover_state(), lambda _: np.zeros(4), 2.0, dt)
    d = xs[-1, 2] - xs[0, 2]
    expect = 0.5 * G * 2.0 ** 2
    ok1 = abs(d - expect) < 1e-6 and np.all(np.isfinite(xs))
    rep.append(("free_fall_2s", ok1, f"down={d:.6f} m expect={expect:.6f} m"))

    # 2. Hover hold: constant thrust = weight along body -z (up in NED).
    def prop_hover(x, u):
        return np.array([0.0, 0.0, -m * G]), np.zeros(3)
    mdl2 = SixDOF(m, I, prop=prop_hover)
    t2, xs2 = mdl2.simulate(hover_state(50.0), lambda _: np.zeros(4), 5.0, dt)
    drift = np.linalg.norm(xs2[-1, 0:3] - xs2[0, 0:3])
    qn = abs(np.linalg.norm(xs2[-1, 6:10]) - 1.0)
    ok2 = drift < 1e-6 and qn < 1e-12 and np.all(np.isfinite(xs2))
    rep.append(("hover_hold_5s", ok2, f"drift={drift:.2e} m quaterr={qn:.2e}"))

    # 3. Scripted tilt sweep (ILLUSTRATIVE manoeuvre, not a controller):
    #    thrust vector rotates body-x/z over 10 s; run must stay finite.
    def prop_tilt(x, u):
        ang = np.clip(x[0] / 50.0, 0, 1) * np.deg2rad(60)
        T = m * G
        return np.array([T * np.sin(ang), 0.0, -T * np.cos(ang)]), np.zeros(3)
    mdl3 = SixDOF(m, I, prop=prop_tilt)
    t3, xs3 = mdl3.simulate(hover_state(100.0), lambda _: np.zeros(4), 10.0, dt)
    ok3 = bool(np.all(np.isfinite(xs3)))
    np.savetxt(out / "tilt_sweep_demo.csv", np.column_stack([t3, xs3]),
               delimiter=",", header="t," + ",".join(
                   ["N", "E", "D", "u", "v", "w", "qw", "qx", "qy", "qz", "p", "q", "r"]))
    rep.append(("tilt_sweep_10s", ok3, "trajectory -> demo/tilt_sweep_demo.csv"))

    # 4. Numerical linearisation at hover trim (finite check only).
    x0 = hover_state(50.0)
    u0 = np.zeros(4)
    f0 = mdl2.derivatives(x0, u0)
    n = 13
    A = np.zeros((n, n))
    eps = 1e-7
    for j in range(n):
        dx = np.zeros(n)
        dx[j] = eps
        A[:, j] = (mdl2.derivatives(x0 + dx, u0) - f0) / eps
    ev = np.linalg.eigvals(A)
    ok4 = bool(np.all(np.isfinite(A)) and np.all(np.isfinite(ev)))
    rep.append(("jacobian_finite", ok4, f"max|Re(ev)|={np.max(np.abs(ev.real)):.3f}"))

    print("6-DOF SMOKE TESTS (implementation checks — NOT model verification)")
    allok = True
    for name, ok, info in rep:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {info}")
        allok &= bool(ok)
    print("STATUS: code runs. Model remains UNVERIFIED (19.15); outputs illustrative only.")
    return allok


def run_verification_cases():
    """19.15-style verification cases with PROPOSED tolerances (TBC).
    Case IDs VC6-001..005 (see HFPX-SIM-VCS-001). Verdicts recorded to
    demo/verification_cases.csv. Passing here is implementation evidence
    ONLY — model registration additionally needs authority data per 19.15.
    """
    from pathlib import Path
    out = Path(__file__).parent / "demo"
    out.mkdir(exist_ok=True)
    m, I, dt = DEMO["mass"], DEMO["inertia"], DEMO["dt"]
    mdl = SixDOF(m, I)
    results = []

    def case(cid, name, tol, val):
        ok = bool(abs(val) <= tol)
        results.append((cid, name, tol, val, "PASS" if ok else "FAIL"))
        return ok

    # VC6-001: free-fall displacement vs analytic (2 s).
    t, xs = mdl.simulate(hover_state(), lambda _: np.zeros(4), 2.0, dt)
    case("VC6-001", "free-fall analytic match", 1e-4,
         (xs[-1, 2] - xs[0, 2]) - 0.5 * G * 2.0 ** 2)
    # VC6-002/003: hover hold drift + quaternion norm (5 s, thrust = weight).
    mdl2 = SixDOF(m, I, prop=lambda x, u: (np.array([0.0, 0.0, -m * G]), np.zeros(3)))
    _, xh = mdl2.simulate(hover_state(50.0), lambda _: np.zeros(4), 5.0, dt)
    case("VC6-002", "hover position drift", 1e-6, np.linalg.norm(xh[-1, 0:3] - xh[0, 0:3]))
    case("VC6-003", "quaternion unit-norm error", 1e-12, abs(np.linalg.norm(xh[-1, 6:10]) - 1.0))
    # VC6-004: mechanical-energy drift in free fall (E = KE - m g h_up).
    v = xs[:, 3:6]
    h_up = -xs[:, 2]
    E = 0.5 * m * np.sum(v ** 2, axis=1) + m * G * h_up
    scale = max(np.max(0.5 * m * np.sum(v ** 2, axis=1)), 1.0)
    case("VC6-004", "energy relative drift", 1e-6, abs(E[-1] - E[0]) / scale)
    # VC6-005: independent Euler cross-check (free fall, loose tolerance).
    x = hover_state()
    dte, n = dt, int(2.0 / dt)
    for _ in range(n):
        x = x + dte * mdl.derivatives(x, np.zeros(4))
    case("VC6-005", "euler cross-check displacement", 0.5,
         abs((x[2] - hover_state()[2]) - 0.5 * G * 2.0 ** 2))

    import csv
    with (out / "verification_cases.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Case", "Name", "Tolerance (PROPOSED TBC)", "Value", "Verdict"])
        w.writerows(results)
    print("6-DOF VERIFICATION CASES (proposed tolerances TBC; implementation evidence only)")
    ok = True
    for cid, name, tol, val, v in results:
        print(f"  [{v}] {cid} {name}: value={val:.3e} tol={tol:.1e}")
        ok &= (v == "PASS")
    return ok


if __name__ == "__main__":
    import sys
    ok = _run_checks()
    ok &= run_verification_cases()
    raise SystemExit(0 if ok else 1)

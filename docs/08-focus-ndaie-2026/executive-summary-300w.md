# Executive Project Summary — AeroPulse-NG (≤300 words, draft)

> Use verbatim or trimmed to fit the online form. Must explain problem, solution, technical approach, likely impact. Current draft: ~195 words — safe under limit.

Nigerian secondary aerodromes and tactical sites lack affordable low-altitude surveillance. Imported primary/secondary radar costs millions, leaves terrain-shadowed and low-traffic gaps, and degrades during harmattan, diversions, and network outages. Non-cooperative targets remain invisible.

AeroPulse-NG is an air-gapped, offline-first tactical radar and airspace surveillance engine that turns a ~$150 commodity SDR and a standard PC into a dual-window ATC/tactical workstation for civil (NAMA-style) and defence users. It ingests 1090 MHz ADS-B/Mode S and 131.55 MHz ACARS over the air, smooths tracks with a 6-state extended Kalman filter plus dead reckoning, detects conflicts with an R*-tree short-term conflict alert, and fuses three weather sources into a 3D matrix with ISA fallback and harmattan dust estimation. Defence overlays cover squawk emergencies, dark-target/silence detection, geofences, and a lead-pursuit intercept solver. No internet is required.

The core is Rust + Tauri with a deterministic replayable engine, single decode path where simulation equals live signal processing, and DuckDB flight recording. The prototype (v2.4.0) is unit-tested with baked demo scenarios and a synthetic-feed mode for pitching without RF hardware. Aligned to Nig.CARs, ICAO Annexes, Doc 4444 separation, DO-260B, and MIL-STD-2525D symbology, it cuts capex by >99% while building locally maintainable sovereign capability and training talent.

Word count: verify in form before submit. Declare generative-AI assistance as required.

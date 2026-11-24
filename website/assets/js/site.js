// BOLTE site: mobile menu, footer year, scroll reveal, reduced-motion handling for animated graphics. No network calls.
(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "Close" : "Menu";
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
      }
    });
  }

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  var items = document.querySelectorAll(".rv, .model");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  if (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.querySelectorAll("svg").forEach(function (svg) {
      if (svg.pauseAnimations) svg.pauseAnimations();
    });
  }
})();

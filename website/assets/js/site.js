// Shared site JS: active nav, year, logo fallback, reduced-motion video. No network. Safe on file://.
(function(){
  "use strict";
  var page = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  document.querySelectorAll("nav.links a").forEach(function(a){
    var href = (a.getAttribute("href") || "").toLowerCase();
    if(href === page || (page === "" && href === "index.html")) a.setAttribute("aria-current","page");
  });
  document.querySelectorAll("[data-year]").forEach(function(el){ el.textContent = new Date().getFullYear(); });
  // Logo fallback: if placeholder PNG missing, show text wordmark (never broken icon).
  document.querySelectorAll("img[data-logo]").forEach(function(img){
    function fallback(){
      var fb = document.createElement("span");
      fb.textContent = "BOLTE";
      fb.style.cssText = "font-weight:800;letter-spacing:.08em";
      if(img.parentNode) img.parentNode.replaceChild(fb, img);
    }
    img.addEventListener("error", fallback);
    if(img.complete && img.naturalWidth === 0) fallback();
  });
  // Respect reduced motion: stop hero video.
  if(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches){
    document.querySelectorAll(".hero video.bg").forEach(function(v){ v.pause(); v.removeAttribute("autoplay"); });
  }
})();

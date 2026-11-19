/* Click / tap an illustration in a post to view it large in an overlay.
   Close with the button, a click outside the image, Esc, or the browser Back button. */
(function () {
  "use strict";
  var imgs = document.querySelectorAll('article img[src*="/assets/img/blog/"]');
  if (!imgs.length) return;

  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  var T = id
    ? { open: "Klik untuk memperbesar gambar", close: "Tutup", dlg: "Gambar diperbesar" }
    : { open: "Click to enlarge the image", close: "Close", dlg: "Enlarged image" };

  var overlay = null, big = null, closeBtn = null, lastFocus = null, isOpen = false;

  function build() {
    overlay = document.createElement("div");
    overlay.className = "img-zoom-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", T.dlg);
    overlay.hidden = true;

    closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.className = "img-zoom-close";
    closeBtn.setAttribute("aria-label", T.close);
    closeBtn.innerHTML = "&times;";

    var box = document.createElement("div");
    box.className = "img-zoom-box";
    big = document.createElement("img");
    big.className = "img-zoom-img";
    box.appendChild(big);

    overlay.appendChild(box);
    overlay.appendChild(closeBtn);
    document.body.appendChild(overlay);

    closeBtn.addEventListener("click", function () { close(true); });
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay || e.target === box) close(true);
    });
  }

  function open(src, alt) {
    if (!overlay) build();
    big.src = src;
    big.alt = alt || "";
    lastFocus = document.activeElement;
    overlay.hidden = false;
    document.documentElement.classList.add("img-zoom-lock");
    isOpen = true;
    try { history.pushState({ imgZoom: 1 }, ""); } catch (e) {}
    closeBtn.focus();
  }

  function close(fromUi) {
    if (!isOpen) return;
    isOpen = false;
    overlay.hidden = true;
    document.documentElement.classList.remove("img-zoom-lock");
    if (fromUi && history.state && history.state.imgZoom) {
      try { history.back(); } catch (e) {}
    }
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  window.addEventListener("popstate", function () { if (isOpen) close(false); });
  document.addEventListener("keydown", function (e) {
    if (isOpen && (e.key === "Escape" || e.key === "Esc")) { e.preventDefault(); close(true); }
  });

  imgs.forEach(function (img) {
    img.classList.add("img-zoomable");
    img.setAttribute("tabindex", "0");
    img.setAttribute("role", "button");
    img.title = T.open;
    img.addEventListener("click", function () { open(img.currentSrc || img.src, img.alt); });
    img.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(img.currentSrc || img.src, img.alt); }
    });
  });
})();

/* Owner-only "Edit" button on posts. Hidden for readers.
   Open any post once with ?edit=1 to switch it on in this browser; ?edit=0 switches it off.
   The button opens the post's source file in GitHub's web editor (new tab). */
(function () {
  "use strict";
  var KEY = "postEditMode";
  var q = location.search;
  try {
    if (/[?&]edit=1(&|$)/.test(q)) localStorage.setItem(KEY, "1");
    if (/[?&]edit=0(&|$)/.test(q)) localStorage.removeItem(KEY);
  } catch (e) {}
  var on = false;
  try { on = localStorage.getItem(KEY) === "1"; } catch (e) {}
  var s = document.currentScript;
  var src = s && s.getAttribute("data-src");
  if (!on || !src) return;
  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  var a = document.createElement("a");
  a.href = "https://github.com/galih-prakoso/galih-prakoso.github.io/edit/main/" + src;
  a.target = "_blank";
  a.rel = "noopener";
  a.textContent = "✎ " + (id ? "Edit tulisan" : "Edit post");
  a.title = id ? "Buka editor GitHub untuk tulisan ini" : "Open this post in the GitHub editor";
  a.style.cssText =
    "position:fixed;right:1rem;bottom:1rem;z-index:9999;padding:.55rem .9rem;border-radius:999px;" +
    "background:#2563eb;color:#fff;font:600 .9rem/1 system-ui,sans-serif;text-decoration:none;" +
    "box-shadow:0 2px 10px rgba(0,0,0,.3);cursor:pointer";
  document.body.appendChild(a);
})();

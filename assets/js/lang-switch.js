/* Language menu: switch to the same page in the other language instead of going back to "about".
   Pages pass the counterpart with data-alt; posts are detected from the cross-language link in the article. */
(function () {
  "use strict";
  var me = document.currentScript;
  var lang = (me && me.getAttribute("data-lang")) || ((document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0 ? "id" : "en");
  var alt = me && me.getAttribute("data-alt");

  function findAlt() {
    if (alt) return alt;
    var re = lang === "en" ? /\/id\/tulisan\/\d{4}\// : /\/blog\/\d{4}\//;
    var links = document.querySelectorAll("article a[href]");
    for (var i = 0; i < links.length; i++) {
      var p = links[i].pathname;
      if (re.test(p)) return links[i].href;
    }
    return null;
  }

  function apply() {
    var target = findAlt();
    document.querySelectorAll(".dropdown-menu a.dropdown-item").forEach(function (a) {
      var isId = /\/id\/?$/.test(a.pathname);
      var isEn = !isId && /^\/?$/.test(a.pathname);
      if (!isId && !isEn) return;
      var wantsOther = (isId && lang === "en") || (isEn && lang === "id");
      if (wantsOther && target) a.setAttribute("href", target);
      else if (!wantsOther) a.setAttribute("href", location.pathname + location.search);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", apply);
  else apply();
  window.addEventListener("load", apply);
})();

// Indonesian navbar for pages under /id/ (theme navbar is English by default).
(function () {
  function run() {
    document.documentElement.lang = "id";
    var map = {
      "/": { href: "/id/", text: "tentang", match: /^\/id\/?$/ },
      "/publications/": { href: "/id/publikasi/", text: "publikasi", match: /^\/id\/publikasi\// },
      "/blog/": { href: "/id/tulisan/", text: "tulisan", match: /^\/id\/(tulisan)\// }
    };
    var path = location.pathname;
    var links = document.querySelectorAll("nav .navbar-nav a.nav-link, nav .navbar-nav a.dropdown-toggle");
    links.forEach(function (a) {
      var url;
      try { url = new URL(a.getAttribute("href") || "", location.origin).pathname; } catch (e) { return; }
      var li = a.closest("li");
      var isToggle = a.classList.contains("dropdown-toggle");
      var item = isToggle ? null : map[url];
      if (item) {
        a.setAttribute("href", item.href);
        // replace only the label text node, keep child elements (e.g. screen-reader "(current)")
        for (var i = 0; i < a.childNodes.length; i++) {
          var n = a.childNodes[i];
          if (n.nodeType === 3 && n.nodeValue.trim()) { n.nodeValue = item.text; break; }
        }
        var isActive = item.match.test(path) || (item.href === "/id/tulisan/" && /^\/id\/tulisan\//.test(path));
        a.classList.toggle("active", isActive);
        if (li) li.classList.toggle("active", isActive);
      } else if (isToggle && /language/i.test(a.textContent)) {
        for (var j = 0; j < a.childNodes.length; j++) {
          var m = a.childNodes[j];
          if (m.nodeType === 3 && /language/i.test(m.nodeValue)) { m.nodeValue = m.nodeValue.replace(/language/i, "bahasa"); break; }
        }
      }
    });
    var brand = document.querySelector("a.navbar-brand");
    if (brand) brand.setAttribute("href", "/id/");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();

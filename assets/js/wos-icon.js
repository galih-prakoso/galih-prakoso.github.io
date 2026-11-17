/* Adds monochrome Web of Science (Clarivate), Scopus and ResearchGate icons to the social icon row, after Google Scholar */
(function () {
  var box = document.querySelector(".contact-icons");
  if (!box || box.querySelector(".extra-icon")) return;
  var icons = [
    { cls: "wos-icon", glyph: "wos-icon-glyph", title: "Web of Science", href: "https://www.webofscience.com/wos/author/record/RKP-4603-2026" },
    /* TODO: replace with the personal Scopus author profile URL once the Scopus Author ID exists */
    { cls: "scopus-icon", glyph: "scopus-icon-glyph", title: "Scopus", href: "https://www.scopus.com/" },
    { cls: "researchgate-icon", glyph: "researchgate-icon-glyph", title: "ResearchGate", href: "https://www.researchgate.net/profile/Galih-Prakoso-7" },
  ];
  var last = box.querySelector('a[href*="scholar.google"]');
  icons.forEach(function (d) {
    var a = document.createElement("a");
    a.className = "extra-icon " + d.cls;
    a.href = d.href;
    a.title = d.title;
    a.target = "_blank";
    a.rel = "external nofollow noopener";
    a.setAttribute("aria-label", d.title);
    var i = document.createElement("i");
    i.className = "extra-icon-glyph " + d.glyph;
    a.appendChild(i);
    if (last) {
      /* same whitespace gap as between the other icons */
      last.after(a);
      last.after(document.createTextNode(" "));
    } else {
      box.appendChild(a);
    }
    last = a;
  });
})();

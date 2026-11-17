/* Adds a monochrome Clarivate (Web of Science) icon to the social icon row, next to Google Scholar */
(function () {
  var box = document.querySelector(".contact-icons");
  if (!box || box.querySelector(".wos-icon")) return;
  var a = document.createElement("a");
  a.className = "wos-icon";
  a.href = "https://www.webofscience.com/wos/author/record/RKP-4603-2026";
  a.title = "Web of Science";
  a.target = "_blank";
  a.rel = "external nofollow noopener";
  a.setAttribute("aria-label", "Web of Science (Clarivate)");
  var i = document.createElement("i");
  i.className = "wos-icon-glyph";
  a.appendChild(i);
  var ref = box.querySelector('a[href*="scholar.google"]');
  if (ref && ref.nextSibling) box.insertBefore(a, ref.nextSibling);
  else box.appendChild(a);
})();

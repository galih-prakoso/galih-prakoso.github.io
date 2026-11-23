/* Make the year, tag and category items of a post header clickable
   (the Indonesian posts render them as plain text). (c) 2026 Galih Prakoso. */
(function () {
  "use strict";
  var box = document.querySelector("p.post-tags");
  if (!box || box.querySelector("a")) return;
  var nodes = Array.prototype.slice.call(box.childNodes);
  nodes.forEach(function (n) {
    if (n.nodeType !== 1 || n.tagName !== "I") return;
    var txt = n.nextSibling;
    if (!txt || txt.nodeType !== 3) return;
    var m = txt.nodeValue.match(/^[\s\u00a0]*([^\s\u00a0\u00b7]+)([\s\S]*)$/);
    if (!m) return;
    var name = m[1];
    var rest = m[2];
    var href = null;
    var cls = n.className || "";
    if (cls.indexOf("fa-hashtag") > -1) href = "/blog/tag/" + encodeURIComponent(name) + "/";
    else if (cls.indexOf("fa-tag") > -1) href = "/blog/category/" + encodeURIComponent(name) + "/";
    else if (cls.indexOf("fa-calendar") > -1) href = "/blog/" + encodeURIComponent(name) + "/";
    if (!href) return;
    var a = document.createElement("a");
    a.href = href;
    box.insertBefore(a, n);
    a.appendChild(n);
    a.appendChild(document.createTextNode(" " + name));
    txt.nodeValue = rest;
  });
})();

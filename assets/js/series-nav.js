/* Previous / next post navigation for the daily series (same language only).
   Reads /assets/json/series.json (built by Jekyll) and adds a small bar near the title
   and larger cards at the end of the post. Nothing is shown if the data is missing. */
(function () {
  "use strict";
  var script = document.currentScript;
  if (!script || !script.src) return;
  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  var L = id
    ? { prev: "Tulisan sebelumnya", next: "Tulisan berikutnya", prevS: "Sebelumnya", nextS: "Berikutnya", aria: "Navigasi seri" }
    : { prev: "Previous post", next: "Next post", prevS: "Previous", nextS: "Next", aria: "Series navigation" };
  var norm = function (p) { return p.replace(/index\.html$/, "").replace(/\/+$/, "") + "/"; };
  var here = norm(location.pathname);
  var dataUrl = new URL("../json/series.json", script.src).href;

  fetch(dataUrl)
    .then(function (r) { return r.ok ? r.json() : []; })
    .then(function (all) {
      var lang = id ? "id" : "en";
      var posts = all.filter(function (p) { return p.lang === lang; });
      var i = -1;
      posts.forEach(function (p, n) { if (norm(p.url) === here) i = n; });
      if (i < 0) return;
      var prev = i > 0 ? posts[i - 1] : null;
      var next = i < posts.length - 1 ? posts[i + 1] : null;
      if (!prev && !next) return;

      var first = document.querySelector("article p");
      if (!first) return;
      var host = first.parentNode;

      function link(cls, post, label, arrow, left) {
        var a = document.createElement("a");
        a.className = cls;
        a.href = post.url;
        a.title = post.title;
        var t = document.createElement("span");
        t.className = "sn-label";
        t.textContent = left ? "\u2039 " + label : label + " \u203A";
        a.appendChild(t);
        return a;
      }

      // compact bar near the title
      var top = document.createElement("nav");
      top.className = "series-nav series-nav-top";
      top.setAttribute("aria-label", L.aria);
      var s1 = document.createElement("span");
      if (prev) s1.appendChild(link("sn-btn", prev, L.prevS, "", true));
      var s2 = document.createElement("span");
      if (next) s2.appendChild(link("sn-btn", next, L.nextS, "", false));
      top.appendChild(s1);
      top.appendChild(s2);
      host.insertBefore(top, first);

      // cards at the end of the post
      var bottom = document.createElement("nav");
      bottom.className = "series-nav series-nav-bottom";
      bottom.setAttribute("aria-label", L.aria);
      function card(post, label, left) {
        var a = document.createElement("a");
        a.className = "sn-card" + (left ? " sn-left" : " sn-right");
        a.href = post.url;
        var k = document.createElement("span");
        k.className = "sn-kicker";
        k.textContent = left ? "\u2039 " + label : label + " \u203A";
        var t = document.createElement("span");
        t.className = "sn-title";
        t.textContent = post.title;
        a.appendChild(k);
        a.appendChild(t);
        return a;
      }
      if (prev) bottom.appendChild(card(prev, L.prev, true));
      if (next) bottom.appendChild(card(next, L.next, false));
      host.appendChild(bottom);
    })
    .catch(function () {});
})();

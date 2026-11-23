/* Share buttons for blog posts. (c) 2026 Galih Prakoso. */
(function () {
  "use strict";
  var first = document.querySelector("article p");
  if (!first) return;
  var host = first.parentNode;
  var isId = location.pathname.indexOf("/id/") === 0;
  var L = isId
    ? { label: "Bagikan tulisan ini", copy: "Salin tautan", copied: "Tautan disalin", native: "Bagikan…" }
    : { label: "Share this post", copy: "Copy link", copied: "Link copied", native: "Share…" };

  var canon = document.querySelector('link[rel="canonical"]');
  var url = (canon && canon.href) || location.origin + location.pathname;
  var h1 = document.querySelector("article h1, h1.post-title");
  var title = (h1 && h1.textContent.trim()) || document.title;
  var u = encodeURIComponent(url);
  var t = encodeURIComponent(title);

  var bar = document.createElement("div");
  bar.className = "share-bar";
  var lab = document.createElement("span");
  lab.className = "share-label";
  lab.textContent = L.label;
  bar.appendChild(lab);

  function add(name, href, cls) {
    var a = document.createElement("a");
    a.className = "share-btn " + cls;
    a.href = href;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.textContent = name;
    bar.appendChild(a);
  }
  add("WhatsApp", "https://wa.me/?text=" + t + "%20" + u, "sh-wa");
  add("Facebook", "https://www.facebook.com/sharer/sharer.php?u=" + u, "sh-fb");
  add("X", "https://twitter.com/intent/tweet?text=" + t + "&url=" + u, "sh-x");
  add("LinkedIn", "https://www.linkedin.com/sharing/share-offsite/?url=" + u, "sh-li");
  add("Telegram", "https://t.me/share/url?url=" + u + "&text=" + t, "sh-tg");

  var cp = document.createElement("button");
  cp.type = "button";
  cp.className = "share-btn sh-copy";
  cp.textContent = L.copy;
  cp.addEventListener("click", function () {
    function ok() {
      cp.textContent = L.copied;
      setTimeout(function () { cp.textContent = L.copy; }, 2000);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(ok, function () { window.prompt(L.copy, url); });
    } else {
      window.prompt(L.copy, url);
    }
  });
  bar.appendChild(cp);

  if (navigator.share) {
    var ns = document.createElement("button");
    ns.type = "button";
    ns.className = "share-btn sh-native";
    ns.textContent = L.native;
    ns.addEventListener("click", function () {
      navigator.share({ title: title, url: url }).catch(function () {});
    });
    bar.insertBefore(ns, bar.children[1]);
  }
  host.appendChild(bar);
})();

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

  var SVGNS = "http://www.w3.org/2000/svg";
  var PATHS = {
    wa: "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z",
    fb: "M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z",
    x: "M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z",
    li: "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
    tg: "M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"
  };
  var STROKES = {
    link: "M10 13a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5 M14 11a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5",
    share: "M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7 M16 6l-4-4-4 4 M12 2v13"
  };
  function icon(kind) {
    var svg = document.createElementNS(SVGNS, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("aria-hidden", "true");
    svg.setAttribute("focusable", "false");
    var p = document.createElementNS(SVGNS, "path");
    if (PATHS[kind]) {
      p.setAttribute("d", PATHS[kind]);
      p.setAttribute("fill", "currentColor");
    } else {
      p.setAttribute("d", STROKES[kind]);
      p.setAttribute("fill", "none");
      p.setAttribute("stroke", "currentColor");
      p.setAttribute("stroke-width", "2");
      p.setAttribute("stroke-linecap", "round");
      p.setAttribute("stroke-linejoin", "round");
    }
    svg.appendChild(p);
    return svg;
  }

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

  function add(name, href, kind) {
    var a = document.createElement("a");
    a.className = "share-btn share-ico sh-" + kind;
    a.href = href;
    a.target = "_blank";
    a.rel = "noopener noreferrer";
    a.title = name;
    a.setAttribute("aria-label", name);
    a.appendChild(icon(kind));
    bar.appendChild(a);
  }
  add("WhatsApp", "https://wa.me/?text=" + t + "%20" + u, "wa");
  add("Facebook", "https://www.facebook.com/sharer/sharer.php?u=" + u, "fb");
  add("X", "https://twitter.com/intent/tweet?text=" + t + "&url=" + u, "x");
  add("LinkedIn", "https://www.linkedin.com/sharing/share-offsite/?url=" + u, "li");
  add("Telegram", "https://t.me/share/url?url=" + u + "&text=" + t, "tg");

  var cp = document.createElement("button");
  cp.type = "button";
  cp.className = "share-btn share-ico sh-copy";
  cp.title = L.copy;
  cp.setAttribute("aria-label", L.copy);
  cp.appendChild(icon("link"));
  cp.addEventListener("click", function () {
    function ok() {
      cp.title = L.copied;
      cp.classList.add("copied");
      setTimeout(function () { cp.title = L.copy; cp.classList.remove("copied"); }, 2000);
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
    ns.className = "share-btn share-ico sh-native";
    ns.title = L.native;
    ns.setAttribute("aria-label", L.native);
    ns.appendChild(icon("share"));
    ns.addEventListener("click", function () {
      navigator.share({ title: title, url: url }).catch(function () {});
    });
    bar.insertBefore(ns, bar.children[1]);
  }
  host.insertBefore(bar, first.nextSibling);
})();

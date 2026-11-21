/* Publication list tweaks (no theme files overridden), applied on About and Publications:
   1) the title links to the original article on the publisher's site (new tab);
   2) a visible "DOI: <number>" line, hyperlinked to the article (new tab);
   3) the separate DOI and HTML buttons are removed (title + DOI line replace them);
   4) the plain "PDF" button becomes a recognisable PDF icon. */
(function () {
  "use strict";
  // Web of Science records, keyed by bibliography entry id.
  var WOS = {
    prakoso2026nesting: "https://www.webofscience.com/wos/woscc/full-record/WOS:001928820200001"
  };
  // Journal home pages, keyed by journal name as shown in the entry.
  var JOURNALS = {
    "Rapid Prototyping Journal": "https://www.emerald.com/rpj"
  };
  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  document.querySelectorAll(".publications li").forEach(function (li) {
    var links = li.querySelectorAll(".links a[href]");
    var external = null;
    var doi = null;
    links.forEach(function (a) {
      var href = a.getAttribute("href");
      if (!external && /^https?:\/\//i.test(href) && a.target === "_blank") external = a.href;
      var m = href.match(/^https?:\/\/(?:dx\.)?doi\.org\/(.+)$/i);
      if (m && !doi) doi = decodeURIComponent(m[1]);
    });

    var title = li.querySelector(".title");
    if (title && external && !title.querySelector("a")) {
      var a = document.createElement("a");
      a.className = "pub-title-link";
      a.href = external;
      a.target = "_blank";
      a.rel = "external nofollow noopener";
      a.title = id ? "Buka artikel asli di situs jurnal" : "Open the original article on the journal website";
      while (title.firstChild) a.appendChild(title.firstChild);
      title.appendChild(a);
    }

    li.querySelectorAll(".periodical em").forEach(function (em) {
      var url = JOURNALS[em.textContent.trim()];
      if (!url || em.querySelector("a")) return;
      var j = document.createElement("a");
      j.className = "pub-journal-link";
      j.href = url;
      j.target = "_blank";
      j.rel = "external nofollow noopener";
      j.title = id ? "Buka situs jurnal" : "Open the journal website";
      while (em.firstChild) j.appendChild(em.firstChild);
      em.appendChild(j);
    });

    var linksBox = li.querySelector(".links");
    if (doi && linksBox && !li.querySelector(".pub-doi")) {
      var d = document.createElement("div");
      d.className = "periodical pub-doi";
      var l = document.createElement("a");
      l.href = "https://doi.org/" + doi;
      l.target = "_blank";
      l.rel = "external nofollow noopener";
      l.textContent = doi;
      l.title = id ? "Buka artikel asli melalui DOI" : "Open the original article via DOI";
      d.appendChild(document.createTextNode("DOI: "));
      d.appendChild(l);
      linksBox.parentNode.insertBefore(d, linksBox);
    }

    var entry = li.querySelector("[id]");
    var wosUrl = entry && WOS[entry.id];
    if (wosUrl && linksBox && !linksBox.querySelector(".wos-btn")) {
      var w = document.createElement("a");
      w.className = "btn btn-sm z-depth-0 wos-btn";
      w.setAttribute("role", "button");
      w.href = wosUrl;
      w.target = "_blank";
      w.rel = "external nofollow noopener";
      w.textContent = "WoS";
      w.title = id ? "Lihat di Web of Science" : "View on Web of Science";
      var pdfLink = null;
      linksBox.querySelectorAll("a[href]").forEach(function (x) {
        if (/\.pdf([?#]|$)/i.test(x.getAttribute("href"))) pdfLink = x;
      });
      linksBox.insertBefore(w, pdfLink);
      linksBox.insertBefore(document.createTextNode(" "), pdfLink);
    }

    links.forEach(function (btn) {
      var href = btn.getAttribute("href");
      if (/^https?:\/\//i.test(href) && btn.target === "_blank") {
        btn.remove(); // DOI / HTML buttons
        return;
      }
      if (/\.pdf([?#]|$)/i.test(href) && !btn.querySelector("i")) {
        btn.classList.add("pdf-btn");
        btn.innerHTML = '<i class="fa-solid fa-file-pdf" aria-hidden="true"></i>';
        btn.setAttribute("aria-label", id ? "Unduh PDF" : "Download PDF");
        btn.title = id ? "Unduh PDF (naskah diterima penulis)" : "Download PDF (author accepted manuscript)";
      }
    });
  });
})();

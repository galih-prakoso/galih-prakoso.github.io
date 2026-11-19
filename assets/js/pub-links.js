/* Publications page tweaks (no theme files overridden):
   1) the title links to the original article on the publisher's site (new tab);
   2) the plain "PDF" button becomes a recognisable PDF icon. */
(function () {
  "use strict";
  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  document.querySelectorAll(".publications li").forEach(function (li) {
    var links = li.querySelectorAll(".links a[href]");
    var external = null;
    links.forEach(function (a) {
      if (!external && /^https?:\/\//i.test(a.getAttribute("href")) && a.target === "_blank") external = a.href;
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

    links.forEach(function (btn) {
      if (/\.pdf([?#]|$)/i.test(btn.getAttribute("href")) && !btn.querySelector("i")) {
        btn.classList.add("pdf-btn");
        btn.innerHTML = '<i class="fa-solid fa-file-pdf" aria-hidden="true"></i>';
        btn.setAttribute("aria-label", id ? "Unduh PDF" : "Download PDF");
        btn.title = id ? "Unduh PDF (naskah diterima penulis)" : "Download PDF (author accepted manuscript)";
      }
    });
  });
})();

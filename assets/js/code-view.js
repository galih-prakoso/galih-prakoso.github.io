/* Shows a companion script inside a post: <div class="code-view" data-src="..."> becomes a
   collapsible block with the source, a Copy button and a Download link.
   The script file itself (with its copyright / licence header) is shown unchanged. */
(function () {
  "use strict";
  var id = (document.documentElement.lang || "en").toLowerCase().indexOf("id") === 0;
  var L = id
    ? { show: "Tampilkan script Python", copy: "Salin", copied: "Tersalin", dl: "Unduh .py", fail: "Script tidak dapat dimuat." }
    : { show: "Show the Python script", copy: "Copy", copied: "Copied", dl: "Download .py", fail: "The script could not be loaded." };

  document.querySelectorAll(".code-view[data-src]").forEach(function (box) {
    var src = box.getAttribute("data-src");
    var name = src.split("/").pop();
    fetch(src)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(function (text) {
        var d = document.createElement("details");
        d.className = "code-view-box";
        var s = document.createElement("summary");
        s.textContent = L.show + " (" + name + ")";
        d.appendChild(s);

        var bar = document.createElement("div");
        bar.className = "code-view-bar";
        var copy = document.createElement("button");
        copy.type = "button";
        copy.textContent = L.copy;
        copy.addEventListener("click", function () {
          var done = function () { copy.textContent = L.copied; setTimeout(function () { copy.textContent = L.copy; }, 1500); };
          if (navigator.clipboard) navigator.clipboard.writeText(text).then(done);
        });
        var dl = document.createElement("a");
        dl.href = src;
        dl.setAttribute("download", name);
        dl.textContent = L.dl;
        bar.appendChild(copy);
        bar.appendChild(dl);
        d.appendChild(bar);

        var pre = document.createElement("pre");
        var code = document.createElement("code");
        code.textContent = text;
        pre.appendChild(code);
        d.appendChild(pre);
        box.textContent = "";
        box.appendChild(d);
      })
      .catch(function () {
        var p = document.createElement("p");
        p.textContent = L.fail + " ";
        var a = document.createElement("a");
        a.href = src;
        a.textContent = name;
        p.appendChild(a);
        box.textContent = "";
        box.appendChild(p);
      });
  });
})();

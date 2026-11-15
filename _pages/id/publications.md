---
layout: page
lang: id
permalink: /id/publikasi/
title: publikasi
description: Publikasi ilmiah (peer-reviewed) dari yang terbaru.
nav: false
---

<p><a href="{{ '/id/' | relative_url }}">Tentang</a> · <a href="{{ '/id/publikasi/' | relative_url }}">Publikasi</a> · <a href="{{ '/id/tulisan/' | relative_url }}">Tulisan</a> · <a href="{{ '/publications/' | relative_url }}">English</a></p>

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

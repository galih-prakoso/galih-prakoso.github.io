---
layout: page
lang: id
permalink: /id/publikasi/
title: publikasi
description: Publikasi ilmiah (peer-reviewed) dari yang terbaru.
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=12">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="id" data-alt="{{ '/publications/' | relative_url }}" defer></script>

<script src="{{ '/assets/js/pub-links.js' | relative_url }}?v=4" defer></script>

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

<p><a href="{{ '/id/' | relative_url }}">Tentang</a> · <a href="{{ '/id/publikasi/' | relative_url }}">Publikasi</a> · <a href="{{ '/id/tulisan/' | relative_url }}">Tulisan</a> · <a href="{{ '/publications/' | relative_url }}">English</a></p>

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

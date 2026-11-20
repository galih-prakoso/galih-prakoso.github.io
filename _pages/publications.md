---
layout: page
permalink: /publications/
title: publications
description: Peer-reviewed publications in reverse chronological order.
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=9">

<script src="{{ '/assets/js/lang-switch.js' | relative_url }}?v=1" data-lang="en" data-alt="{{ '/id/publikasi/' | relative_url }}" defer></script>

<script src="{{ '/assets/js/pub-links.js' | relative_url }}?v=3" defer></script>

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

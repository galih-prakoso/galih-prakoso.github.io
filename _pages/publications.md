---
layout: page
permalink: /publications/
title: publications
description: Peer-reviewed publications in reverse chronological order.
nav: true
nav_order: 2
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=6">

<script src="{{ '/assets/js/pub-links.js' | relative_url }}?v=1" defer></script>

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>

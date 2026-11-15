---
layout: page
lang: id
permalink: /id/tulisan/
title: tulisan
description: Catatan harian dan artikel tentang optimasi, teknik industri, dan manufaktur.
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=2">

<script src="{{ '/assets/js/lang-nav-id.js' | relative_url }}" defer></script>

<p><a href="{{ '/id/' | relative_url }}">Tentang</a> · <a href="{{ '/id/publikasi/' | relative_url }}">Publikasi</a> · <a href="{{ '/id/tulisan/' | relative_url }}">Tulisan</a> · <a href="{{ '/blog/' | relative_url }}">English</a></p>

{% assign id_posts = site.posts | where: "lang", "id" %}

{% if id_posts.size == 0 %}

Belum ada tulisan.

{% else %}

<ul class="post-list" style="list-style: none; padding-left: 0;">
  {% for post in id_posts %}
  <li style="margin-bottom: 1.5rem;">
    <h3 style="margin-bottom: 0.25rem;"><a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="post-meta" style="margin-bottom: 0.25rem;">{{ post.date | date: "%Y-%m-%d" }}</p>
    <p style="margin-bottom: 0.25rem;">{{ post.description }}</p>
    <p style="margin-bottom: 0.5rem;"><a class="read-more" href="{{ post.url | relative_url }}">Baca selengkapnya &rarr;</a></p>
    <p class="post-tags" style="margin-bottom: 0;">
      {% for tag in post.tags %}<i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }} &nbsp;{% endfor %}
    </p>
  </li>
  {% endfor %}
</ul>

{% endif %}

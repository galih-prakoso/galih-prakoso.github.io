---
layout: page
permalink: /blog/
title: writing
description: Daily notes and articles on optimization, industrial engineering, and manufacturing.
nav: true
nav_order: 3
---

<link rel="stylesheet" href="{{ '/assets/css/justify.css' | relative_url }}?v=2">

{% assign en_posts = site.posts | where: "lang", "en" %}

{% if en_posts.size == 0 %}

No posts yet.

{% else %}

<ul class="post-list" style="list-style: none; padding-left: 0;">
  {% for post in en_posts %}
  <li style="margin-bottom: 1.5rem;">
    <h3 style="margin-bottom: 0.25rem;"><a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="post-meta" style="margin-bottom: 0.25rem;">{{ post.date | date: "%B %-d, %Y" }}</p>
    <p style="margin-bottom: 0.25rem;">{{ post.description }}</p>
    <p style="margin-bottom: 0.5rem;"><a class="read-more" href="{{ post.url | relative_url }}">Read more &rarr;</a></p>
    <p class="post-tags" style="margin-bottom: 0;">
      {% for tag in post.tags %}<i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }} &nbsp;{% endfor %}
    </p>
  </li>
  {% endfor %}
</ul>

{% endif %}

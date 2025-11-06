---
title: Meme of the Monday
layout: page
permalink: /meme-of-the-monday/
noindex: true
---

A historical preservation project remembering a period in which the passage of time for our group of friends was measured not in weeks, but in memes.

<ol>
{% assign ordered = site.motm | sort: "order" %}
{% for doc in ordered %}
  <li><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></li>
{% endfor %}
</ol>

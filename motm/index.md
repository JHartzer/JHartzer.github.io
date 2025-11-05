---
title: Meme of the Monday
layout: page
permalink: /meme-of-the-monday/
---

<ol>
{% assign ordered = site.motm | sort: "order" %}
{% for doc in ordered %}
  <li><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></li>
{% endfor %}
</ol>

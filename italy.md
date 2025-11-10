---
title: Italy Fish 2015
layout: page
permalink: /italy/
noindex: true
---

<p align="center" style="font-size: 1.5em;"><i>
Something something ... auld lang syne ... something ... for old times sake
</i></p>

<ol>
{% assign ordered = site.italy | sort: "order" %}
{% for doc in ordered %}
  <li><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></li>
{% endfor %}
</ol>

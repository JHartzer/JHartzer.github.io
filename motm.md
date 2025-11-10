---
title: Meme of the Monday
layout: page
permalink: /meme-of-the-monday/
noindex: true
---

<p align="center" style="font-size: 1.5em;"><i>
A historical preservation project remembering a period in which the passage of time for our group of friends was measured not in weeks, but in memes.
</i></p>

<ol>
{% assign ordered = site.motm | sort: "order" %}
{% for doc in ordered %}
  <li><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></li>
{% endfor %}
</ol>

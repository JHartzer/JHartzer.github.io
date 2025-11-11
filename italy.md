---
title: Italy Fish 2015
layout: page
permalink: /italy/
noindex: true
---

<i>
This blog is written by the students of the Champe Fitzhugh International Honors Leadership Seminar. It is intended to give those back home a taste of our international adventures, and provide an outlet for reflection on this whirlwind journey. We hope you enjoy our posts as much as we are enjoying our travels! Ciao amici!
</p>

<ol>
{% assign ordered = site.italy | sort: "order" %}
{% for doc in ordered %}
  <li><a href="{{ doc.url | relative_url }}">{{ doc.title }}</a></li>
{% endfor %}
</ol>

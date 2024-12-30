---
layout: page
title: Posts
permalink: /posts/
---

{% for post in site.posts %}
<li>
    <p style="text-align:left;">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
        <a href="{{ post.url }}">{{ post.title }}</a>
    </p>
</li>
{% endfor %}

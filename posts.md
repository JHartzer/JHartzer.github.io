---
layout: page
title: Posts
permalink: /posts/
---

<ul>
{% for post in site.posts %}

{% assign tags = post.tags | join: "" %}
{%- if post != site.posts[0] -%}
<hr>
{%- endif -%}
<br>
<li>
    <div style="width: 100%; overflow: hidden;">
        {%- if post.thumbnail -%}
        <div style="width: 70%; float: left;">
        {% else %}
        <div style="width: 100%; float: left;">
        {%- endif -%}
            <h3>
                <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <p class="post-meta">
            {%- if post.description -%}
            {{ post.description }}
            <br>
            {%- endif -%}
            {{ post.date | date: "%Y-%m-%d" }}
            {% if tags != "" %}
            <br>
            {% for tag in post.tags %}
                <a href="{{ tag | slugify | prepend: '/tags/#' | prepend: site.baseurl}}">
                <i class="fas fa-hashtag fa-sm"></i> {{ tag }}</a> &nbsp;
            {% endfor %}
            {% endif %}
            </p>
        </div>
        {%- if post.thumbnail -%}
        <div style="margin-left:: 30%;">
            <img class="card-img" src="{{post.thumbnail | relative_url}}" style="object-fit: scale-down; height: 90px; background-color: white" alt="thumbnail image not available">
        </div>
        {%- endif -%}
    </div>
</li>
<br>
{% endfor %}
</ul>
<br>


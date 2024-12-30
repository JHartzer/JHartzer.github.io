---
layout: page
title: Home
permalink: /
---

Howdy! My name is Jacob Hartzer, and I am a Mechanical Engineering PhD Student. I am originally from Austin, Texas, and also attended Texas A&M for my undergraduate and master’s degrees in Mechanical Engineering. My background interests were originally in controls and dynamics, which slowly led me to estimation and filtering. My professional and research experience has also given me avenues to use coding skills to apply these interests to real-world problems in simulated and fielded environments.

Currently, I am researching localization and calibration techniques using kalman filter based methods. Specifically, I am trying to incorporate real time estimation of state with the monitoring of sensor calibration and health in a way that is optimal and computationally efficient. I am also interested in the development of monte-carlo simulations for algorithm validation, as well as open-source software packages to share this work.

Most of my work focuses on the simulation and estimation of complex dynamic systems. I spend much of my time in work and research coding custom models in a number of environments. This has allowed me to contribute to more accurate estimation and localization of these systems and improve the development of new devices with more accurate models.

<h2>Latest Posts</h2>

{% for post in site.posts limit: 3 %}
<li>
    <p style="text-align:left;">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
        <a href="{{ post.url }}">{{ post.title }}</a>
    </p>
</li>
{% endfor %}


<div class="contact-icons">
{%- if site.github -%}
<a href="https://github.com/{{ site.github }}" title="GitHub"><i class="fab fa-github"></i></a>
{% endif %}
{%- if site.linkedin -%}
<a href="https://www.linkedin.com/in/{{ site.linkedin }}" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
{% endif %}
{%- if site.semanticscholar -%}
<a href="https://www.semanticscholar.org/author/{{ site.semanticscholar }}" title="Semantic Scholar"><i class="ai ai-semantic-scholar"></i></a>
{% endif %}
{%- if site.orcid -%}
<a href="https://orcid.org/{{ site.orcid }}" title="ORCID"><i class="ai ai-orcid"></i></a>
{% endif %}
{%- if site.rss_icon -%}
<a href="{{ site.baseurl }}/feed.xml" title="RSS Feed"><i class="fas fa-rss-square"></i></a>
{% endif %}
</div>

---
layout: page
title: Home
permalink: /
---

<img src="/assets/img/profile.jpg" alt="Profile Picture" style="float:right;width:200px"/>

Howdy! My name is Jacob Hartzer, and I am a Mechanical Engineer by education and a Roboticist by trade. I am originally from Austin, Texas and attended Texas A&M for my undergraduate through Ph.D. degrees in Mechanical Engineering. My background interests were originally in controls and dynamics, which slowly led me to estimation and filtering. My professional and research experience has also given me avenues to use coding skills to apply these interests to real-world problems in simulated and fielded environments.

My past research interesets were in localization and calibration techniques using kalman filter based methods. Specifically, I incorporated real time estimation of state with the monitoring of sensor calibration and health in a way that is optimal and computationally efficient. I also explored the development of monte-carlo simulations for algorithm validation, as well as developed open-source software packages to share this work.

Most of my current work focuses on the simulation and estimation of complex autonomous systems. I spend much of my time in work coding custom models in a number of environments to deliver mission autonomy to multi-national customers. This has allowed me to contribute to more accurate estimation and localization of these systems and improve the development of new devices with more accurate models.

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
<a href="https://github.com/{{ site.github }}" title="GitHub"><svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" width="48px" height="48px"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path fill="white" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg></a>
{% endif %}
{%- if site.linkedin -%}
<a href="https://www.linkedin.com/in/{{ site.linkedin }}" title="LinkedIn"><svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="48px" height="48px"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path fill="white" d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"/></svg></a>
{% endif %}
{%- if site.semanticscholar -%}
<a href="https://www.semanticscholar.org/author/{{ site.semanticscholar }}" title="Semantic Scholar"><svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="48px" height="48px"><path fill="white"  d="m 379.0868,75.20191 c 18.16812,40.68422 25.53302,83.89034 32.42143,127.20955 -1.26557,0.35902 -2.52865,0.72116 -3.79427,1.08267 -0.9109,-2.53364 -1.98432,-5.02156 -2.70735,-7.60959 -5.21805,-18.65384 -10.47938,-37.29655 -15.47376,-56.01156 -1.79641,-6.7327 -6.03443,-10.08392 -12.09539,-13.38137 -8.90177,-4.84112 -17.31343,-11.08316 -24.69005,-18.04576 -4.70771,-4.44068 -8.73494,-7.14859 -15.41325,-7.07815 -44.46061,0.47028 -88.92553,0.51538 -133.38426,0.92448 -2.96314,0.0295 -6.63075,1.12345 -8.72809,3.06448 -8.08853,7.48476 -15.67094,15.51457 -25.64177,25.55586 26.29927,64.04074 39.52245,133.8403 33.84523,208.04469 -12.62623,-8.0842 -22.40117,-14.47949 -22.98144,-31.41848 C 177.54002,222.87779 151.42365,146.31401 96.863089,80.431113 95.635828,78.948619 95.025884,76.955074 94.126122,75.20129 H 379.0868 Z M 48.729955,107.84705 c 12.662672,0 25.33214,-0.20085 37.983708,0.17178 2.510789,0.0723 6.022658,1.66788 7.277148,3.67935 37.836649,60.79088 67.333839,124.63574 71.155359,197.68268 0.0178,0.28921 -0.2826,0.59448 -1.36262,2.71657 -22.61129,-77.29358 -63.40364,-142.73587 -115.871175,-201.39106 0.273676,-0.95167 0.544426,-1.90519 0.818185,-2.85871 z m -40.7293523,53.1819 c 18.0890173,-0.65752 33.3891773,-1.3175 48.6911883,-1.60238 1.541204,-0.0295 3.360468,2.009 4.650795,3.4439 29.847587,33.20131 56.935394,68.2806 73.632114,110.23473 3.17758,7.97976 5.35158,16.35996 7.98907,24.55477 C 108.37943,243.23533 60.253096,202.53752 7.9999987,161.02833 Z M 202.47422,436.79811 c -31.48153,-50.06559 -61.80372,-98.28894 -92.12778,-146.5123 0.37077,-0.47706 0.74155,-0.95165 1.11169,-1.42811 2.54233,2.04731 56.62149,45.41225 80.9093,65.30201 6.76608,5.54129 11.87848,5.44178 18.91585,-0.27375 82.58396,-67.08545 174.73706,-117.86224 272.58287,-158.80848 5.22305,-2.18511 10.64009,-3.91664 15.98238,-5.81688 1.18651,-0.42022 2.44093,-0.65319 4.15147,-0.22122 C 390.37701,255.0261 281.97764,327.27773 202.47359,436.79871 Z" style="stroke-width:0.0868161"/></svg></a>
{% endif %}
{%- if site.orcid -%}
<a href="https://orcid.org/{{ site.orcid }}" title="ORCID"><svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="48px" height="48px"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path fill="white" d="M294.8 188.2h-45.9V342h47.5c67.6 0 83.1-51.3 83.1-76.9 0-41.6-26.5-76.9-84.7-76.9zM256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm-80.8 360.8h-29.8v-207.5h29.8zm-14.9-231.1a19.6 19.6 0 1 1 19.6-19.6 19.6 19.6 0 0 1 -19.6 19.6zM300 369h-81V161.3h80.6c76.7 0 110.4 54.8 110.4 103.9C410 318.4 368.4 369 300 369z"/></svg></a>
{% endif %}
{%- if site.rss_icon -%}
<a href="{{ site.baseurl }}/feed.xml" title="RSS Feed"><svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="48px" height="48px"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path fill="white" d="M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM96 136c0-13.3 10.7-24 24-24c137 0 248 111 248 248c0 13.3-10.7 24-24 24s-24-10.7-24-24c0-110.5-89.5-200-200-200c-13.3 0-24-10.7-24-24zm0 96c0-13.3 10.7-24 24-24c83.9 0 152 68.1 152 152c0 13.3-10.7 24-24 24s-24-10.7-24-24c0-57.4-46.6-104-104-104c-13.3 0-24-10.7-24-24zm0 120a32 32 0 1 1 64 0 32 32 0 1 1 -64 0z"/></svg></a>
{% endif %}
</div>


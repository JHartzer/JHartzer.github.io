---
layout: post
title: How I built a Website using Jekyll
date: 2020-06-23
thumbnail: /assets/img/jekyll.png
tags: Programming
date: 2020-06-23
description:
tags:
categories:
related_posts: false
---

<img src="/assets/img/jekyll.png" alt="Jekyll" style="float:right;width:25%"/>

A mechanical engineer with a website, how peculiar you might say! I promise it's
easy and you can do the same. This is a static-site hosted on github pages that
I can easily edit and push changes to using my home desktop. It is build using 
a Ruby Gem called [jekyll](https://jekyllrb.com/) which really was the catalyst
for me to create this site. If something this good looking had to be created 
from scratch, I would still be stuck in mid-2000's html land. 

## Install Jekyll

I would recommend following the jekyll 
[Quick Start Guide](https://jekyllrb.com/docs/) for instructions on setting up a 
Ruby environment, bundler, and jekyll. This is a relatively painless process, 
and can be done on any OS. 

## Create your site

The way that I built this site and the way I recommend others to is to start 
with a template and then modify it to meet your own particular needs. There are 
sites that aggregate [jekyll themes](http://jekyllthemes.org/) that can be used
or purchased. I forked my site template from Dean Attali's 
[beautiful-jekyll](https://github.com/daattali/beautiful-jekyll#readme) which has 
really expanded my perspective of what is possible using a static site. 
Responsive design and consideration for phones were not things that I had 
originally anticipated when I started looking into the css, but I am glad that 
I had a foundation to modify and experiment with. 

## Advanced Generation 

Jekyll uses the [Liquid](https://shopify.github.io/liquid/) template language 
to process templates. You can read jekyll's documentation 
[here](https://jekyllrb.com/docs/liquid/). The biggest takeaways, in my opinion,
are the use of liquid variables to iterate through build pages, and define
how certain pages are to be treated.  


## In Short

Jekyll makes build a static site extremely easy, and GitHub has removed the cost
normally associated with hosting a site. There's nothing to lose, so good luck 
and go try it! 
---
layout: post
title: "Poseidon's Orbital Kiss"
tags:
render_latex: true
---

*Don't ask me why this was on my mind, I have to deal with my thoughts and now so do you*

Anyways, have you ever experienced a *Poseidon's Kiss*? In simple terms, it's when you're using the toilet, and the stool dropping into the bowl causes a jet of water to rush up and splash right where everything originated. Well, I've wondered for some time exactly how high this jet of water could go. Unfortunately, that's a very difficult science problem involving surface tension, hydrodynamics, etc.

But I am still an engineer, which means I can just make assumptions until I am able to solve a problem and then just draw a box around it and call it done. So, I will instead solve the much easier problem of *How much water could the average stool send into orbit, assuming no frictional losses?* Great question! Let me tell you.

So first, how fast are we talking? To achieve **Low Earth Orbit (LEO)**, our liquid payload needs to reach roughly **7,800 m/s**. For perspective, that’s about 23 times the speed of sound. If your toilet water actually hit this speed, the resulting shockwave would likely deconstruct the porcelain, and your bathroom, into a fine ceramic mist long before the water left the bowl. To maximize the stool-powered water launcher, assume perfect energy transfer and (critically) neglect atmospheric drag. Additionally, assume the following values:

### The Energy Source

- **Mass ($m_{s}$):** $0.4\text{ kg}$ (a healthy, robust contribution).
- **Drop Height ($h$):** $0.3\text{ meters}$ (from the "launch pad" to the water line).
- **Gravity ($g$):** $9.8\text{ m/s}^2$.

With this, the total potential energy ($U$) is calculated as:

$$
\begin{split}
U &= m_{s} \cdot g \cdot h \\
U &= 0.4 \cdot 9.8 \cdot 0.3 \\
U &\approx 1.18\text{ Joules}
\end{split}
$$

### Orbital Velocity

The kinetic energy ($K$) required to achieve orbit depends on that staggering velocity of $7,800\text{ m/s}$. To find the mass ($m_{w}$) of water that could hit orbital speeds using our $1.18\text{ J}$ of energy, we use the kinetic energy formula:

$$K = \frac{1}{2} m_{w} v^2$$

Rearranging for $m_{w}$:

$$
\begin{split}
m_{w} &= \frac{2K}{v^2} \\
m_{w} &= \frac{2 \cdot 1.18}{7,800^2} \\
m_{w} &\approx 3.88 \times 10^{-8}\text{ kg} \\
m_{w} &\approx 0.0388\text{ mg}
\end{split}
$$

That is roughly **0.038 milligrams** of water. For context, a single standard raindrop is about $50\text{ mg}$. This is approximately half the weight of a single grain of salt. So, your morning routine could theoretically launch a miniscule mist into orbit, or at least the amount of dignity remaining after the splash.


### Takeaways

Next time you experience this aquatic phenomenon, don’t be annoyed. Be proud! You aren't just a victim of fluid displacement; you are a localized energy generator capable of accelerating matter to speeds that would make NASA sweat!

**Pro-tip:** To decrease the "Delta-V" of the return splash, consider deploying a "landing pad" of toilet paper to dampen the kinetic transfer. Credit: [Poop Splash Elimination - Smarter Every Day 22](https://www.youtube.com/watch?v=-XNDM4eAn1U)

---
layout: post
title:  Autonomous Cone Placement
thumbnail: /assets/img/ConeSetup.png
tags: [Localization]
date: 2020-03-07
description:
tags:
categories:
related_posts: false
---

<img src="/assets/img/ConeSetup.png" alt="cone" style="float:right;width:30%"/>

The Auto Cone project is an effort to develop cones that are capable of localizing and placing themselves to improve safety conditions for highway workers. These cones utilize RTK GPS and onboard localization filtering to produce decimeter-level accuracy in placing themselves in road conditions. Additionally, they are capable of transitioning through GPS-denied environments such as under bridges or overpasses. Pictured are two of the cones and the real-time kinematic (RTK) base station.

# Problem:

<img src="/assets/img/Kinematics.png" alt="Kinematics" style="float:right;width:30%"/>

The goal of this project is to develop a robotic platform capable of automatically placing cones in a defined wedge shape behind the work vehicle within the starting lane. Specifically the cones shall: 
- Place three cones in 40 foot increments in a wedge
- Begin the wedge 80 feet from the end of the vehicle
- Operate on highway surfaces unaffected by small debris
- Remain within the lane despite road curvature
- Not rely on magnetic or road-embedded sensors
- Have a speed greater than 0.3 m/s
- Cost less than $1,500 per cone unit
- Be easy to use and require little training


# Kinematics:

The omnidirectional platform makes the system holonomic, which means that with only three motors, the system can smoothly and directly move between any two states. This allows orientation to be independently controlled from position, and makes the system unconstrained by initial conditions. This is very advantageous for pick and place when deploying. The image outlines the kinematics used to drive the cone's motion. 

# Sensor Fusion:

<img src="/assets/img/RTK.png" alt="RTK GPS" style="float:right;width:30%"/>

Using a system of RTK GPS and a ground base station, the cone's achieve a much lower position error than typical GPS for a relatively small increase in cost. 

Fusing these corrected GPS measurements with the higher rate encoders on the wheel motors provides the system with a high rate localization estimate that is robust in handling drift and sensor noise. 

# Results:

The results of this project were a functioning prototype system that is capable of deploying multiple cones without collision to a wedge shape formation while remaining within lane lines. The system is also capable of operating in GPS-denied environments. 

# Videos

Deployment: 
<iframe width="560" height="315" src="https://www.youtube.com/embed/0hgOc2csaWE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The IV 2020 presentation slides are available [here]({{site.baseurl}}/assets/pdf/2020-06-IV.pdf) and recording is available here:
<iframe width="560" height="315" src="https://www.youtube.com/embed/cbcMwYcLUmk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Citation:

```bibtex
@inproceedings{2020_AutoCone,
  author    = {Hartzer, Jacob and Saripalli, Srikanth},
  booktitle = {2020 IEEE Intelligent Vehicles Symposium (IV)},
  title     = {AutoCone: An OmniDirectional Robot for Lane-Level Cone Placement},
  year      = {2020},
  pages     = {1663-1668},
  doi       = {10.1109/IV47402.2020.9304683},
}
```
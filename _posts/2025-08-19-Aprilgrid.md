---
layout: post
title: Detecting Aprilgrids in C++
author: Jacob Hartzer
date: 2025-08-19
description:
tags:
categories:
related_posts: false
---

I'm excited to announce the release of my [Aprilgrid](https://github.com/JHartzer/aprilgrid) detection library, a lightweight, cross-platform library for detecting and processing Aprilgrids (of [Kalibr](https://github.com/ethz-asl/kalibr/) fame) in images and point clouds.

<p align="center">
  <img src="/assets/img/aprilgrid_25h9_4x6_out.png" style="float:center"/>
</p>


With this library, you can:
- Detect [AprilTags](https://github.com/AprilRobotics/apriltag) with subpixel accuracy
- Estimate pose and orientation of detected grids
- Draw tag and grid detections
- Generate Aprilgrid images

Written in C++ and using OpenCV 4.6.0+, this library is cross platform, can be easily integrated into ROS, and supports tags using any of OpenCV's  four [pre-defined April tag dictionaries](https://docs.opencv.org/4.6.0/d9/d6a/group__aruco.html#gac84398a9ed9dd01306592dd616c2c975) (16h5, 25h9, 36h10, or 36h11)

Perfect for sensor calibration, robotics, autonomous vehicles, or mapping, the repository is FOSS and is available [here](https://github.com/JHartzer/aprilgrid). Let me know if you'd like to contribute or if you have questions!

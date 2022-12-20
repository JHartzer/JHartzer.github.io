---
layout: post
title:  Online Multi-Camera and IMU Calibration
author: Jacob Hartzer
image: /assets/img/multi_cam_imu/setup_thumb.png
---

This research focuses on the implementation of an online multi-camera IMU calibration filter that is based on the work of [Mirzaei and Roumeliotis](https://doi.org/10.1109/IROS.2007.4399342). This work expands on what has been previously done by incorporating the fiducial marker detectors provided by [OpenCV](https://opencv.org/) and manipulating the update equations to utilize the quaternion measurement provided by these detectors.

<img src="/assets/img/multi_cam_imu/setup.png" alt="UWB Ranging" style="float:right;width:40%"/>

The main challenge was in developing the Jacobians for the quaternion measurement, such that the updates would be stable even with large body rotations. To overcome this challenge, the derivations and work by Joan Sola which can be found on [ArXiv](https://arxiv.org/abs/1711.02508) were used extensively.

Additionally, work was performed on monitoring the calibration for shifts in extrinsic parameters, such as would occur if a sensor is bumped in the middle of use. Through the use of a sliding window T-test, online monitoring of calibration extrinsic parameters was implemented.  

## Experimentation
<img src="/assets/img/multi_cam_imu/8020.png" alt="UWB Ranging" style="float:right;width:40%"/>

Testing was performed using a bar of 8020 with multiple camera mounts and a IMU/INS. This allowed for multiple sensor configurations and rapid recalibration testing with different sensor configurations. The specific sensors tested were:
- IMUs:
  - Vectornav VN300 
  - Vectornav VN100 
  - Wheeltec FDISystems N100N
  - Pixhawk PX4
  - WitMotion WT901C485
- Cameras: 
  - Flir Blackfly BFLY-PGE-20E4C-CS 
  - Basler Ace acA1920-40uc 

## Code

The code has been open-sourced and is available on [Github](https://github.com/unmannedlab/multi-cam-imu-cal). Feel free to fork, update and create pull requests where you see fit, so long as you adhere to the GPL3 license.

## Preprint

A preprint of the published paper can be found on [ArXiv](https://arxiv.org/abs/2209.13821).

## Citation:

```
@INPROCEEDINGS{9564981,
  author={Hartzer, Jacob and Saripalli, Srikanth},
  booktitle={2022 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR)}, 
  title={Online Multi Camera-IMU Calibration}, 
  year={2022}
```
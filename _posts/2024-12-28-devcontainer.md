---
layout: post
title: Testing code in devcontainers using Docker
author: Jacob Hartzer
# thumbnail: /assets/img/multi_imu.png
date: 2024-12-28
description:
tags: Docker
categories:
related_posts: false
---

From time to time I review open sourced projects for the Journal of Open Source Software (JOSS). This is usually a productive endeavor where I get to explore some unknown branch of research and the associated software being written to actually perform the research. Just like there is a wide array of topics I get to review, there is also a large variance in quality of the code being submitted. With that said, I don't necessarily want to install the entire dependency tree in order to review a single repository. That is where [devcontainers](https://code.visualstudio.com/docs/devcontainers/create-dev-containers) come in.

This development method allows VS Code to be run inside a docker container such that all the dependencies can be exactly installed as required by the software I'm evaluating. The basic structure within VS Code is to have a `devcontainer.json` file within the `.vscode` directory. While not necessary, I also generally define a custom [Dockerfile](https://docs.docker.com/reference/dockerfile/) in that directory as well since I usually am installing additional dependencies on top of a base container. The `devcontainer.json` I generally use is


```json
{
    "name": "Docker-env",
    "build": {
        "dockerfile": "Dockerfile"
    },
    "workspaceMount": "src=${localWorkspaceFolder},dst=/${localWorkspaceFolder}_ws/src/${localWorkspaceFolder},type=bind,consistency=cached",
    "workspaceFolder": "/${localWorkspaceFolder}_ws/src/${localWorkspaceFolder}"
}
```

Where the workspaceMount and workspaceFolder items are useful for defining where the workspace should be mounted within the docker container. This is very useful when working with ROS/colcon packages that expect the workspace to be in a specific location to be built.

The `Dockerfile` follows from a basic alpine container, but I will use different base images based on the repo being worked on (e.g. using the osrf ROS images, or a Jekyll container).

```Dockerfile
FROM alpine:latest

# non interactive frontend for locales
ENV DEBIAN_FRONTEND=noninteractive

# installing texlive and utils
RUN apt-get update && \
    apt-get -y install \
    *all-apt-dependencies*
    && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install *all-python-dependencies*
```
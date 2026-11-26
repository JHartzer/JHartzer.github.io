FROM ubuntu:latest

# non interactive frontend for locales
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install \
    build-essential \
    git \
    jekyll \
    ruby ruby-dev \
    -y

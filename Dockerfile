FROM ubuntu:latest

# non interactive frontend for locales
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -y install \
    ruby \
    jekyll \
    git

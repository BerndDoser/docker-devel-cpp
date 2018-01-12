FROM bernddoser/docker-devel-cpp:ubuntu-16.04

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

FROM nvidia/cuda:8.0-devel

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    curl \
    git \
    make \
    software-properties-common \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget https://cmake.org/files/v3.9/cmake-3.9.1-Linux-x86_64.tar.gz \
 && tar xf cmake-3.9.1-Linux-x86_64.tar.gz \
 && rm cmake-3.9.1-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.9.1-Linux-x86_64/bin/cmake /usr/bin/cmake

WORKDIR /

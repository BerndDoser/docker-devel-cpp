FROM ubuntu:16.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    automake \
    build-essential \
    bzip2 \
    curl \
    git \
    libz-dev \
    libbz2-dev \
    libopenmpi-dev \
    make \
    openmpi-bin \
    openmpi-common  \
    openssh-client \  
    software-properties-common \
    unzip \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/cmake-3.7.2 \
 && cd /opt/cmake-3.7.2 \
 && wget https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz \
 && tar xf cmake-3.7.2-Linux-x86_64.tar.gz \
 && rm cmake-3.7.2-Linux-x86_64.tar.gz

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-4.9 g++-4.9 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-4.9 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-4.9 /usr/bin/gcc

ENTRYPOINT ["cat"]


FROM ubuntu:17.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

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

RUN wget https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz \
 && tar xf cmake-3.7.2-Linux-x86_64.tar.gz \
 && rm cmake-3.7.2-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.7.2-Linux-x86_64/bin/cmake /usr/bin/cmake

WORKDIR /

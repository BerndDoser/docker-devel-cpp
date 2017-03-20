FROM ubuntu:17.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-7 g++-7 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-7 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-7 /usr/bin/gcc


FROM bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.7.2

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-5 g++-5 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-5 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-5 /usr/bin/gcc


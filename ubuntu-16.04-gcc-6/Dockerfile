FROM bernddoser/docker-devel-cpp:ubuntu-16.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-6 g++-6 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-6 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-6 /usr/bin/gcc

ENV CC gcc
ENV CXX g++

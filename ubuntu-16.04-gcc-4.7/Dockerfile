FROM bernddoser/docker-devel-cpp:ubuntu-16.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-4.7 g++-4.7 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-4.7 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-4.7 /usr/bin/gcc

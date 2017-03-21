FROM bernddoser/docker-devel-cpp:ubuntu-17.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-add-repository -y ppa:ubuntu-toolchain-r/test \
 && apt-get update \
 && apt-get install -y gcc-7 g++-7 \
 && apt-get clean \
 && ln -sf /usr/bin/g++-7 /usr/bin/g++ \
 && ln -sf /usr/bin/gcc-7 /usr/bin/gcc


FROM bernddoser/docker-devel-cpp:ubuntu-17.04-gcc-7

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    python-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -I conan==0.26.1 

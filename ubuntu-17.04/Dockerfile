FROM ubuntu:17.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    curl \
    git \
    make \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


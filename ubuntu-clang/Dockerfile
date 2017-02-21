FROM ubuntu:16.04

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    automake \
    build-essential \
    bzip2 \
    curl \
    git \
    libboost-all-dev \
    libbz2-dev \
    libopenmpi-dev \
    libz-dev \
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
 && rm cmake-3.7.2-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.7.2/cmake-3.7.2-Linux-x86_64/bin/cmake /usr/bin/cmake

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y clang-3.9 lldb-3.9 \
 && apt-get clean \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.9 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.9 100


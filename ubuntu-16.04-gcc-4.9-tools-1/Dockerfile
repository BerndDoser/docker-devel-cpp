FROM bernddoser/docker-devel-cpp:ubuntu-16.04-gcc-4.9

MAINTAINER Bernd Doser <bernd.doser@h-its.org>

RUN apt-get update \
 && apt-get install -y \
    doxygen \
    git \
    libboost-all-dev \
    libopenblas-dev \
    make \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz \
 && tar xf cmake-3.7.2-Linux-x86_64.tar.gz \
 && rm cmake-3.7.2-Linux-x86_64.tar.gz \
 && ln -sf /opt/cmake-3.7.2-Linux-x86_64/bin/cmake /usr/bin/cmake

WORKDIR /tmp

RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz \
 && tar xf release-1.8.0.tar.gz \
 && rm release-1.8.0.tar.gz \
 && cd googletest-release-1.8.0 \
 && mkdir build \
 && cd build \
 && cmake -DCMAKE_INSTALL_PREFIX=/opt/googletest-1.8.0 .. \
 && make -j \
 && make install \
 && rm -r /tmp/googletest-release-1.8.0

# Reset link from base container, because one of the installed packages install gcc-5 and overwrite it
RUN ln -sf /usr/bin/gcc-4.9 /usr/bin/gcc

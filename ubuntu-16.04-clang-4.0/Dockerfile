FROM bernddoser/docker-devel-cpp:ubuntu-16.04

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-4.0 main" >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y clang-4.0 lldb-4.0 \
 && apt-get clean \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-4.0 100 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-4.0 100

ENV CC clang
ENV CXX clang++

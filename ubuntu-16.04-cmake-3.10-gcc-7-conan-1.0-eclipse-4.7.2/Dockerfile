FROM bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    curl \
    libgtk2.0-0 \
    make \
    openjdk-8-jdk \
    python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip \
 && pip3 install -I pyyaml==3.12 

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/oxygen/2/eclipse-cpp-oxygen-2-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

# Install plugins
ADD install_plugins.py plugins.yml /
RUN ./install_plugins.py

# Config conan
ENV CONAN_USER_HOME /root
RUN conan remote add conan-community https://api.bintray.com/conan/conan-community/conan

CMD $INSTALLATION_DIR/eclipse/eclipse

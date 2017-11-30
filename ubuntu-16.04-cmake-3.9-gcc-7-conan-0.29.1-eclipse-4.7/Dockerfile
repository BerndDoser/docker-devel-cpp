FROM bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.9-gcc-7-conan-0.29.1

LABEL maintainer="Bernd Doser <bernd.doser@braintwister.eu>"

RUN apt-get update \
 && apt-get install -y \
    curl \
    libgtk2.0-0 \
    make \
    openjdk-8-jdk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/oxygen/R/eclipse-cpp-oxygen-R-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN curl -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR

ADD install_plugins.sh /root/install_plugins.sh
RUN sh /root/install_plugins.sh

# Create eclipse user
RUN mkdir -p /home/eclipse \
 && groupadd -r eclipse \
 && useradd -r -g eclipse -d /home/eclipse -s /sbin/nologin -c "Docker image user" eclipse
RUN chown eclipse:eclipse /home/eclipse
USER eclipse
WORKDIR /home/eclipse

ENV CONAN_USER_HOME /home/eclipse

CMD $INSTALLATION_DIR/eclipse/eclipse

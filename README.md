# docker-devel-cpp

## DEPRECATION NOTICE

:exclamation:
**Please find the new repository at** https://github.com/BrainTwister/docker-devel-env

Docker enables a great way for fast, small, reproducable, and portable software development environments.

The advantages are:

 * Fast build and execution of containers, especially compared to virtual machines
 * Very economical consumption of resources
 * Portability: Same environment on differerent machines and different plattform (also different operating systems)
 * Identical environment for IDE and continuous integration
 * Easy provisioning 
 * Reproducable behaviors

## Requirements

 * docker
 * docker-compose (recommened)

## Docker image structure

The docker images are structured modular with the syntax
`module1` - `version1` - `module2` - `version2` - `module3` - `version3` - `...`,
where image `module1-version1-module2-version2-module3-version3` is using the image
`module1-version1-module2-version2` as base. The name of the directory is used
as docker image label, so that it can be pulled with

```bash
docker pull bernddoser/docker-devel-cpp:module1-version1-module2-version2-module3-version3
```

## Eclipse IDE

A ready-for-action eclipse IDE with 

 * CMake
 * GCC
 * conan.io
 * docker-engine

installed can be started by

```bash
docker run -e /tmp/.X11-unix:/tmp/.X11-unix:ro -D DISPLAY bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0-docker-17.12-eclipse-4.7.2
```

or using docker-compose by

```yaml
version: "3"
services:

  eclipse:
    image: bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.10-gcc-7-conan-1.0-docker-17.12-eclipse-4.7.2
    volumes:
      - /tmp/.X11-unix:/tmp/.X11-unix:ro 
      - /var/run/docker.sock:/var/run/docker.sock
      - home:/home/eclipse:rw
    environment:
      - DISPLAY

volumes:
  home:
```

## Jenkins build container

A declarative Jenkinsfile can look like

```groovy
pipeline {

  agent {
    docker {
      image 'bernddoser/docker-devel-cpp:ubuntu-16.04-cmake-3.10-clang-6-conan-1.0'
    }
  }

  stages {
    stage('Conan') {
      steps {
        sh 'conan install .'
      }
    }
    stage('CMake') {
      steps {
        sh 'cmake .'
      }
    }
    stage('Build') {
      steps {
        sh 'make all'
      }
    }
    stage('Test') {
      steps {
        sh 'make test'
      }
    }
  }
}
```

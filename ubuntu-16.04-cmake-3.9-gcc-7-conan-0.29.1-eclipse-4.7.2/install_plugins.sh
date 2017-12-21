#!/bin/bash

$INSTALLATION_DIR/eclipse/eclipse \
-noSplash -clean -purgeHistory \
-application org.eclipse.equinox.p2.director \
-destination $INSTALLATION_DIR/eclipse \
-repository \
https://raw.githubusercontent.com/15knots/cmakeed/master/cmakeed-update/ \
-installIU \
com.cthing.cmakeed.feature.feature.group \
org.eclipse.cdt.docker.launcher.source.feature.group \
-tag docker_initial

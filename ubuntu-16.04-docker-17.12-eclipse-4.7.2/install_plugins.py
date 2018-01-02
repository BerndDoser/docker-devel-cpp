#!/usr/bin/python3

import subprocess
import yaml

stream = open('plugins.yml', 'r')
plugins = yaml.load(stream)

for plugin in plugins:
  cmd = "$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse -repository " \
      + plugin['repo'] \
      + " -installIU"

  for unit in plugin['units']:
    cmd += " " + unit

  cmd += " -tag docker_initial"
  
  subprocess.run(cmd, shell=True, check=True)

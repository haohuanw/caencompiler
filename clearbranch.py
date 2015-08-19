#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from caencompiler.modes.clearbranchmode import *

def main():
    stream = file('config.yaml','r')
    config = yaml.load(stream)
    clearBranch(config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH_GIT"]) 

if __name__ == "__main__":
    main()

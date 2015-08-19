#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from caencompiler.test.gitlocaltest import gitlocaltest
from caencompiler.test.constantstest import uploadTest
from fabric.api import *
import yaml
# from app.modes.gitmode import GitMode
# from app.modes.uploadmode import UploadMode
def main():
    stream = file('config.yaml','r')
    config = yaml.load(stream)
    # gitlocaltest(config["PROJECT_LOCAL_PATH"])
    uploadTest("all", "proj1", "proj1", ["io.cpp", "io.h", "proj1.cpp"], \
            config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH_UPLOADS"],\
            config["host"], config["user"], config["passwords"])
    # GitMode.compile("all","proj1","proj1")
    # UploadMode.compile("all", "proj1", "proj1", ["io.cpp", "io.h", "proj1.cpp"])

if __name__ == '__main__':
    main()

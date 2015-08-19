#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from caencompiler.test.gitlocaltest import gitlocaltest
from caencompiler.test.constantstest import uploadTest, GitTest
from fabric.api import *
import yaml
# from app.modes.gitmode import GitMode
# from app.modes.uploadmode import UploadMode
def main():
    stream = file('config.yaml','r')
    config = yaml.load(stream)
    # gitlocaltest(config["PROJECT_LOCAL_PATH"])
    # uploadTest("all", "proj1", "proj1", ["io.cpp", "io.h", "proj1.cpp"], \
            # config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH_UPLOADS"],\
            # config["host"], config["user"], config["passwords"])
    GitTest("all", "proj1", "proj1", \
            config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH_GIT"],\
            config["host"], config["user"], config["passwords"])


if __name__ == '__main__':
    main()

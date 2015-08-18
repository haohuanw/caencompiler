#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from app.test.gitlocaltest import gitlocaltest
from app.test.constantstest import constantsremotetest
from fabric.api import *
from constants import *
from app.modes.gitmode import GitMode
from app.modes.uploadmode import UploadMode
def main():
    # GitMode.compile("all","proj1","proj1")
    UploadMode.compile("all", "proj1", "proj1", ["io.cpp", "io.h", "proj1.cpp"])

if __name__ == '__main__':
    main()

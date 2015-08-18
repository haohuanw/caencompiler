#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from app.test.gitlocaltest import gitlocaltest
from app.test.constantstest import constantsremotetest
from fabric.api import *
from constants import *
from app.modes.gitmode import GitMode
def main():
    GitMode.compile("all","./proj1","proj1")

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from app.test.gitlocaltest import gitlocaltest
from app.test.constantstest import constantsremotetest
from fabric.api import *
from constants import *

def main():
    # gitlocaltest()
    constantsremotetest()

if __name__ == '__main__':
    main()

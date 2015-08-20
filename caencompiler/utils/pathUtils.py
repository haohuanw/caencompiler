#!/usr/bin/env python
# -*- coding: utf-8 -*-

# make path end with /
def makeGoodPath(path):
    if path.endswith('/'):
        return path
    return path+'/'

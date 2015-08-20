#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ExeError(Exception):
    def __init__(self, output):
        self.output = output
    def __str__(self):
        return repr(self.output)

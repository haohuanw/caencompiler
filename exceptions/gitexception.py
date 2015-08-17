#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GitError(Exception):
    def __init__(self, directory, output):
        self.directory = directory
        self.output = output
    def __str__(self):
        return repr((self.directory, self.output))


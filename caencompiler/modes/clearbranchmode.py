#!/usr/bin/env python
# -*- coding: utf-8 -*-

from caencompiler.models.gitcommands import *

class ClearBranchMode:
    def __init__(self, localPath, remotePath):
        self.g = GitCommands(localPath, remotePath)

    def process(self):
       self.g.checkLocalMaster()
       self.g.deleteLocalBranch()
       self.g.deleteRemoteBranch()

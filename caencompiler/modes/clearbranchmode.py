#!/usr/bin/env python
# -*- coding: utf-8 -*-

from caencompiler.models.gitcommands import *

def clearBranch(localPath, remotePath):
    g = GitCommands(localPath, remotePath)
    g.checkLocalMaster()
    g.deleteLocalBranch()
    g.deleteRemoteBranch()

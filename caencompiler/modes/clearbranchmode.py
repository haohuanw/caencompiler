#!/usr/bin/env python
# -*- coding: utf-8 -*-

from caencompiler.models.gitcommands import *

def clearLocalBranch(path):
    g = GitLocalCommands(path)
    g.checkMaster()
    g.deleteLocalBranch()
    g.deleteRemoteBranch()

def clearRemoteBranch(path):
    g = GitRemoteCommands(path)
    g.checkoutMaster()

def clearBranch(localPath, remotePath):
    clearLocalBranch(localPath)
    clearRemoteBranch(remotePath)

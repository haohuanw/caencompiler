#!/usr/bin/env python
# -*- coding: utf-8 -*-
from caencompiler.models.gitcommands import GitLocalCommands

def gitlocaltest(path):
    G = GitLocalCommands(path) 
    G.createBranch()
    G.pushBranch()
    G.checkMaster()
    G.deleteLocalBranch()
    G.deleteRemoteBranch()


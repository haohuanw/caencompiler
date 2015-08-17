#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.models.gitcommands import GitLocalCommands

def gitlocaltest():
    GitLocalCommands.createBranch()
    GitLocalCommands.pushBranch()
    GitLocalCommands.deleteBranch()


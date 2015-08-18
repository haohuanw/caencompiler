#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models.gitcommands import *
from constants import *

class ClearBranchMode:

    @staticmethod
    def clearbranch():
        GitLocalCommands.checkMaster()
        GitLocalCommands.deleteLocalBranch()
        GitLocalCommands.deleteRemoteBranch()

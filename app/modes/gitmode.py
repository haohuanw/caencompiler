#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models.gitcommands import *
from app.models.execommands import *
from fabric.context_managers import *
from constants import *

class GitMode:

    @staticmethod
    def compile(name, execution, subfolder):
        with settings(host_string = host):
            GitLocalCommands.createBranch()
            GitLocalCommands.pushBranch()
            
            GitRemoteCommands.pullBranch()
            GitRemoteCommands.checkoutCaenBranch()
            exe = ExeCommands(name, execution, subfolder, True) 
            makeresult = exe.make()
            executeresult = exe.execute()
            GitRemoteCommands.checkoutMaster()
            
            GitLocalCommands.checkMaster()
            GitLocalCommands.deleteLocalBranch()
            GitLocalCommands.deleteRemoteBranch()

            print makeresult
            print executeresult

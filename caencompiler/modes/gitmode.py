#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from caencompiler.models.gitcommands import *
from caencompiler.models.execommands import *
from fabric.context_managers import *

class GitMode:
    def __init__(self, name, execution, subfolder, localPath, remotePath):
        self.G = GitCommands(localPath, remotePath)
        self.exe = ExeCommands(name, execution, subfolder, remotePath)

    def clearBranch(self):
        self.G.checkRemoteMaster()
        self.G.checkLocalMaster() 
        self.G.deleteLocalBranch()
        self.G.deleteRemoteBranch()

    def compile(self, host, user, passwords):
        with settings(host_string = host):

            self.G.createLocalBranch()
            self.G.pushLocalBranch()
            self.G.pullRemoteBranch()
            self.G.checkCaenBranch()
            
            makeresult = self.exe.make()
            if not makeresult.succeeded:
                self.clearBranch()
                print makeresult
                sys.exit(1)

            executeresult = self.exe.execute()
            if not executeresult.succeeded:
                self.clearBranch()
                print makeresule
                print executeresult
                sys.exit(1)

            self.clearBranch()
            print makeresult
            print executeresult

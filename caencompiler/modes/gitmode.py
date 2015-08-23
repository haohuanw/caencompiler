#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fabric.context_managers import settings, hide 
from caencompiler.models.gitcommands import GitCommands 
from caencompiler.models.execommands import ExeCommands
from caencompiler.models.dircommands import DirCommands
from caencompiler.exceptions.direxception import DirError

class GitMode:
    def __init__(self, name, execution, subfolder, localPath, remotePath):
        self.G = GitCommands(localPath, remotePath+'git/')
        self.exe = ExeCommands(name, execution, subfolder, remotePath+'git/')
        self.remote = remotePath

    def clearBranch(self):
        self.G.checkRemoteMaster()
        self.G.checkLocalMaster() 
        self.G.deleteLocalBranch()
        self.G.deleteRemoteBranch()

    def compile(self, host, user, passwords, isVerbose):
        if isVerbose:
            _setting = settings(host_string = host)
        else:
            _setting = settings(hide('everything'), host_string = host) 
        with _setting:
            if DirCommands.isGitInit(self.remote):
                self.process(isVerbose)
            else:
                raise DirError("Git mode is not init in the remote path.")
            
    def process(self, isVerbose):
        if isVerbose:
            print "Create local branch"
        self.G.createLocalBranch()
        if isVerbose:
            print "Push local branch"
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
            print makeresult
            print executeresult
            sys.exit(1)

        if isVerbose:
            print "Clear branches"
        self.clearBranch()
        print makeresult
        print executeresult


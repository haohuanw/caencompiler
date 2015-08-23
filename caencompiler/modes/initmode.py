#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.context_managers import settings, hide
from caencompiler.models.initcommands import InitCommands
from caencompiler.models.dircommands import DirCommands
from caencompiler.exceptions.direxception import DirError

class InitMode:
    def __init__(self, gitAddr, localAddr, remotePath):
        InitCommands.remote = remotePath
        self.I = InitCommands()
        self.gitAddr = gitAddr
        self.localAddr = localAddr
        self.remote = remotePath

    def compile(self, host, user, passwords, isGit, isVerbose):
        if isVerbose:
            _setting = settings(host_string = host)
        else:
            _setting = settings(hide('everything'), host_string = host) 
        with _setting:
            if isGit:
                if not DirCommands.isGitInit(self.remote) and len(self.gitAddr) > 0:
                    self.processGit()
                else:
                    raise DirError("Already init git mode in the remote path.")
            else:
                if not DirCommands.isUploadInit(self.remote):
                    self.processUpload()
                else:
                    raise DirError("Already init upload mode in the remote path.")

    def processGit(self):
        self.I.createFolders()
        self.I.cloneGit(self.gitAddr)

    def processUpload(self):
        self.I.createFolders()
        self.I.cpUpload(self.localAddr)
            

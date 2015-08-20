#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from caencompiler.models.dircommands import DirCommands
from caencompiler.exceptions.direxception import DirError
from caencompiler.exceptions.gitexception import GitError

class InitCommands:
    remote = ""
    def __init__(self, gitaddr):
        if len(InitCommands.remote) == 0:
            raise DirError('Create InitCommands Failed, dont have valid path')
        self.gitAddr = gitaddr 

    def createFolders(self):
        direct = InitCommands.remote
        if direct.endswith('/'):
            direct = direct[:len(direct)-1]
        createProcess = []
        while len(direct) > 0:
            if DirCommands.isRemoteDirectExist(direct):
                break
            else:
                splitName = direct.rsplit('/',1)
                direct = splitName[0]
                if len(splitName[1]) != 0:
                    createProcess.append(splitName[1])
            
        if len(direct) == 0:
            raise DirError('Cannot create directory')

        while len(createProcess) > 0:
            with cd(direct):
                ret = run("mkdir %s" % createProcess[-1])
                if not ret.succeeded:
                    raise DirError(ret)
                if direct.endswith('/'):
                    direct += createProcess.pop()
                else:
                    direct += '/' + createProcess.pop()
        
    def cloneGit(self):
        if DirCommands.isRemoteDirectExist(InitCommands.remote+'git/') and \
                DirCommands.isRemoteDirectExist(InitCommands.remote+'uploads/'):
            return
        elif DirCommands.isRemoteDirectExist(InitCommands.remote):
            with cd(InitCommands.remote):
                ret = run("git clone %s git" % self.gitAddr)
                if not ret.succeeded:
                    raise GitError(InitCommands.remote, ret)
                ret = run("mkdir uploads")
                if not ret.succeeded:
                    raise GitError(InitCommands.remote, ret)
                ret = run("cp -r git/ uploads/")
                if not ret.succeeded:
                    raise GitError(InitCommands.remote, ret)



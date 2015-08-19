#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from functools import wraps
from caencompiler.exceptions.direxception import DirError
from caencompiler.exceptions.gitexception import GitError
from caencompiler.models.dircommands import DirCommands
from fabric.api import run, cd

# def atPath(path):
def gitAtLocal(f):
    @wraps(f)
    def decorated(self, **kwargs):
        if os.getcwd() != self.local:
            try:
                DirCommands.enterDirAbs(self.local)
            except DirError as e:
                print "Directory Error: ,", e.output
        return f(self, **kwargs)
    return decorated
    # return decorator


class GitCommands:

    def __init__(self, localPath, remotePath):
        self.local = localPath
        self.remote = remotePath

    def testLocal(self):
        (status, output) = commands.getstatusoutput("mkdir tmp")
        if status != 0:
            raise GitError(os.getcwd(), output)

    @gitAtLocal
    def checkLocalMaster(self):
        (status, output) = commands.getstatusoutput("git checkout master")
        if status != 0:
            raise GitError(os.getcwd(), output)

    @gitAtLocal
    def createLocalBranch(self):
        (status, output) = commands.getstatusoutput("git checkout -b caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd(), output) 

    @gitAtLocal
    def pushLocalBranch(self):
        (status, output) = commands.getstatusoutput("git push origin caencompile_submit:caencompile_submit")
        if status != 0:
            self.checkLocalMaster()
            self.deleteLocalBranch()
            raise GitError(os.getcwd, output) 

    @gitAtLocal
    def deleteLocalBranch(self):
        GitLocalCommands.checkMaster()
        (status, output) = commands.getstatusoutput("git branch -D caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd, output) 

    @gitAtLocal
    def deleteRemoteBranch(self):
        GitLocalCommands.checkMaster()
        (status, output) = commands.getstatusoutput("git push origin :caencompile_submit ")
        if status != 0:
            raise GitError(os.getcwd, output) 

    def testRemote(self):
        with cd(self.remote):
            ret = run("ls")
            if ret.succeeded:
                return ret
            else:
                raise GitError(self.remote, ret)
    
    def pullRemoteBranch(self):
        with cd(self.remote):
            ret = run("git pull origin caencompile_submit")
            if ret.succeeded:
                return ret
            else:
                self.checkLocalMaster()
                self.createLocalBranch()
                self.deleteRemoteBranch()
                raise GitError(self.remote, ret)

    def checkCaenBranch(self):
        with cd(self.remote):
            ret = run("git checkout origin/HEAD")
            if ret.succeeded:
                return ret
            else:
                self.checkRemoteMaster()
                self.checkLocalMaster()
                self.createLocalBranch()
                self.deleteRemoteBranch()
                raise GitError(self.remote, ret)


    def checkRemoteMaster(self):
        with cd(self.remote):
            ret = run("git checkout master")
            if ret.succeeded:
                return ret
            else:
                raise GitError(self.remote, ret)


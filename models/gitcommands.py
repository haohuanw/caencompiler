#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from constants import env, PROJECT_LOCAL_PATH, PROJECT_REMOTE_PATH
from exceptions.gitexception import GitError 
from models.dircommands import atlocaldirect

class GitLocalCommands:

    @staticmethod
    @atlocaldirect
    def checkMaster():
        (status, output) = commands.getstatusoutput("git checkout master")
        if status != 0:
            raise GitError(os.getcwd(), output)

    @staticmethod
    @atlocaldirect
    def createBranch():
        (status, output) = commands.getstatusoutput("git checkout -b caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd(), output) 

    @staticmethod
    @atlocaldirect
    def pushBranch():
        (status, output) = commands.getstatusoutput("git push origin caencompile_submit:caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd, output) 

    @staticmethod
    @atlocaldirect
    def deleteBranch():
        self.checkMaster()
        (status, output) = commands.getstatusoutput("git branch -D caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd, output) 

class GitRemoteCommands:

    def __init__(self):
        pass

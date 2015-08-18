#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from constants import CAEN_USER_DIRECTORY, PROJECT_LOCAL_PATH, PROJECT_REMOTE_PATH_GIT
from app.exceptions.gitexception import GitError
from app.models.dircommands import atlocalproject
from fabric.api import run, cd

class GitLocalCommands:

    @staticmethod
    def test():
        (status, output) = commands.getstatusoutput("mkdir tmp")
        if status != 0:
            raise GitError(os.getcwd(), output)

    @staticmethod
    @atlocalproject
    def checkMaster():
        (status, output) = commands.getstatusoutput("git checkout master")
        if status != 0:
            raise GitError(os.getcwd(), output)

    @staticmethod
    def createBranch():
        (status, output) = commands.getstatusoutput("git checkout -b caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd(), output) 

    @staticmethod
    @atlocalproject
    def pushBranch():
        (status, output) = commands.getstatusoutput("git push origin caencompile_submit:caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd, output) 

    @staticmethod
    @atlocalproject
    def deleteLocalBranch():
        GitLocalCommands.checkMaster()
        (status, output) = commands.getstatusoutput("git branch -D caencompile_submit")
        if status != 0:
            raise GitError(os.getcwd, output) 

    @staticmethod
    @atlocalproject
    def deleteRemoteBranch():
        GitLocalCommands.checkMaster()
        (status, output) = commands.getstatusoutput("git push origin :caencompile_submit ")
        if status != 0:
            raise GitError(os.getcwd, output) 


class GitRemoteCommands:

    @staticmethod
    def test():
        with cd(CAEN_USER_DIRECTORY+"Documents"):
            return run("ls")
    
    @staticmethod
    def pullBranch():
        with cd(PROJECT_REMOTE_PATH_GIT):
            run("git pull origin caencompile_submit")

    @staticmethod
    def checkoutCaenBranch():
        with cd(PROJECT_REMOTE_PATH_GIT):
            run("git checkout origin/HEAD")

    @staticmethod
    def checkoutMaster():
        with cd(PROJECT_REMOTE_PATH_GIT):
            run("git checkout master")


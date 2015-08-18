#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from constants import env, PROJECT_LOCAL_PATH, PROJECT_REMOTE_PATH
from app.exceptions.gitexception import GitError
from app.models.dircommands import atlocalproject
from fabric.api import run

class GitLocalCommands:

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
    def pullBranch():
        with cd(PROJECT_REMOTE_PATH):
            run("git pull origin caencompile_submit")

    @staticmethod
    def checkoutCaenBranch():
        with cd(PROJECT_REMOTE_PATH):
            run("git checkout origin/caencompile_submit")

    @staticmethod
    def checkoutMaster():
        with cd(PROJECT_REMOTE_PATH):
            run("git checkout master")


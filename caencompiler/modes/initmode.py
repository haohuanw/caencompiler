#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.context_managers import settings
from caencompiler.models.initcommands import InitCommands

class InitMode:
    def __init__(self, gitAddr, remotePath):
        InitCommands.remote = remotePath
        self.I = InitCommands(gitAddr)

    def compile(self, host, user, passwords):
        with settings(host_string = host):
            self.process()

    def process(self):
        self.I.createFolders()
        self.I.cloneGit()

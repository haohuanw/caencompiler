#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

class ExeCommands:
     
    def __init__(self, name, execution, subfolder, remotePath):
        self.makename = name
        self.execommand = execution
        if subfolder.startswith('/'):
            if subfolder[1:]:
                self.folder = subfolder[1:]
            else:
                self.folder = ""
        self.folder = subfolder
        self.remotePath = remotePath + self.folder
    
    def make(self):
        with cd(self.remotePath):
            return run('make clean && make %s' % self.makename)

    def execute(self):
        with cd(self.remotePath):
            return run('./%s' % self.execommand)

        

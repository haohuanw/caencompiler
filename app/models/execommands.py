#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants import PROJECT_REMOTE_PATH_GIT, PROJECT_REMOTE_PATH_UPLOADS

class ExeCommands:
     
    def __init__(self, name, execution, subfolder, isGit):
        self.makename = name
        self.execommand = execution
        if subfolder.startswith('/'):
            if subfolder[1:]:
                self.folder = subfolder[1:]
            else:
                self.folder = ""
        self.folder = subfolder
        self.isGit = isGit
    
    def make(self):
        if self.isGit:
            with cd(PROJECT_REMOTE_PATH_GIT+self.folder):
                return run('make clean && make %s' % self.makename)
        else:
            with cd(PROJECT_REMOTE_PATH_UPLOADS+self.folder):
                return run('make clean && make %s' % self.makename)

    def execute(self):
        if self.execommand is not None:
            if self.isGit:
                with cd(PROJECT_REMOTE_PATH_GIT+self.folder):
                    return run('./%s' % self.execommand)
            else:
                with cd(PROJECT_REMOTE_PATH_UPLOADS+self.folder):
                    return run('./%s' % self.execommand)

        

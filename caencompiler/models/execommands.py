#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from fabric.api import *
from caencompiler.models.dircommands import DirCommands
from caencompiler.exceptions.exeexception import ExeError

def exeAtRemote(f):
    @wraps(f)
    def decorated(self, **kwargs):
        if not DirCommands.isRemoteDirectExist(self.remote):
            raise ExeError("Remote path not exist")
        return f(self, **kwargs)
    return decorated

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
        self.remote = remotePath + self.folder
    
    @exeAtRemote
    def make(self):
        with cd(self.remote):
            ret =  run('make clean && make %s' % self.makename)
            if ret.succeeded:
                return ret
            else:
                raise ExeError(ret)

    @exeAtRemote
    def execute(self):
        if len(self.execommand) == 0:
            return 
        with cd(self.remote):
            ret = run('%s' % self.execommand)
            if ret.succeeded:
                return ret
            else:
                raise ExeError(ret)


        

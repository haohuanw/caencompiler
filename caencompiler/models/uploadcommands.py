#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from functools import wraps
from fabric.api import put
from caencompiler.models.dircommands import DirCommands
from caencompiler.exceptions.direxception import DirError

def uploadAtLocal(f):
    @wraps(f)
    def decorated(self, **kwargs):
        if os.getcwd() != self.local:
            try:
                DirCommands.enterDirAbs(self.local)
            except DirError as e:
                print "Directory Error: ,", e.output
        return f(self, **kwargs)
    return decorated


class UploadCommands:

    def __init__(self,subfolder,files, localPath, remoteUploadsPath):
        if subfolder.startswith('/'):
            if subfolder[1:]:
                self.folder = subfolder[1:]
            else:
                self.folder = ""
        self.folder = subfolder
        self.local = localPath + self.folder + '/'
        self.remote = remoteUploadsPath + self.folder + '/'
        self.filelist = files

    @uploadAtLocal
    def transferFiles(self):
        for f in self.filelist:
            ret = put(self.local+f,self.remote+f)
            if not ret.succeeded:
                print ret
                sys.exit(1)


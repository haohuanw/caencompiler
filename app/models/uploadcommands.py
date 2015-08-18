#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import put
from constants import *

class UploadCommands:

    def __init__(self,subfolder,files):
        if subfolder.startswith('/'):
            if subfolder[1:]:
                self.folder = subfolder[1:]
            else:
                self.folder = ""
        self.folder = subfolder
        self.filelist = files

    def transferFiles(self):
        for f in self.filelist:
            put(PROJECT_LOCAL_PATH+self.folder+'/'+f,PROJECT_REMOTE_PATH_UPLOADS+self.folder+'/'+f)



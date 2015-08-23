#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from fabric.context_managers import settings, hide 
from caencompiler.models.dircommands import DirCommands
from caencompiler.models.uploadcommands import UploadCommands
from caencompiler.models.execommands import ExeCommands
from caencompiler.exceptions.direxception import DirError

class UploadMode:
    def __init__(self, name, execution, subfolder, files, localPath, remoteUploadsPath):
        self.up = UploadCommands(subfolder, files, localPath, remoteUploadsPath+'uploads/')
        self.exe = ExeCommands(name, execution, subfolder, remoteUploadsPath+'uploads/')
        self.remote = remoteUploadsPath

    def compile(self, host, user, passwords, isVerbose):
        if isVerbose:
            _setting = settings(host_string = host)
        else:
            _setting = settings(hide('everything'), host_string = host)
        with _setting:
            if DirCommands.isRemoteDirectExist(self.remote):
                self.process()
            else:
                raise DirError("Upload mode is not init in the remote path.")
    
    def process(self):
        self.up.transferFiles()
        makeresult = self.exe.make()
        if not makeresult.succeeded:
            print makeresult
            sys.exit(1)

        executeresult = self.exe.execute()
        if not executeresult.succeeded:
            print makeresult
            print executeresult
            sys.exit(1)

        print makeresult
        print executeresult


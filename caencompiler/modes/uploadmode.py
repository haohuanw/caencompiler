#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from caencompiler.models.uploadcommands import *
from caencompiler.models.execommands import *
from fabric.context_managers import *

class UploadMode:
    def __init__(self, name, execution, subfolder, files, localPath, remoteUploadsPath):
        self.up = UploadCommands(subfolder, files, localPath, remoteUploadsPath)
        self.exe = ExeCommands(name, execution, subfolder, remoteUploadsPath)

    def compile(self, host, user, passwords):
        with settings(host_string = host):
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

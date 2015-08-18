#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.models.uploadcommands import *
from app.models.execommands import *
from fabric.context_managers import *
from constants import *

class UploadMode:

    @staticmethod
    def compile(name, execution, subfolder, files):
        with settings(host_string = host):
            up = UploadCommands(subfolder, files)
            up.transferFiles()
            exe = ExeCommands(name, execution, subfolder, False)
            makeresult = exe.make()
            executeresult = exe.execute()
            print makeresult
            print executeresult

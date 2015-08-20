#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from fabric.contrib import files
from caencompiler.exceptions.direxception import DirError

class DirCommands:

    @staticmethod
    def isLocalDirectExist(direct):
        return os.path.exists(direct) 

    @staticmethod
    def isRemoteDirectExist(direct):
        return files.exists(direct) 

    @staticmethod
    def enterDirAbs(direct):
        (status, output) = commands.getstatusoutput("cd %s" % direct)
        if status != 0:
            raise DirError(output)


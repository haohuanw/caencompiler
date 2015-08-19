#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from caencompiler.exceptions.direxception import DirError

class DirCommands:
    @staticmethod
    def enterDirAbs(direct):
        (status, output) = commands.getstatusoutput("cd %s" % direct)
        if status != 0:
            raise DirError(output)



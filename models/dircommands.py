#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import commands
from exceptions.direxception import DirError
from constants import PROJECT_LOCAL_PATH, PROJECT_REMOTE_PATH

class DirCommands:
    @staticmethod
    def enterDirAbs(direct):
        (status, output) = commands.getstatusoutput("cd %s" % direct)
        if status != 0:
            raise DirError(output)

def atlocalproject(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if os.getcwd() != PROJECT_LOCAL_PATH:
            try:
                DirCommands.enterDirAbs(PROJECT_LOCAL_PATH)
            except DirError as e:
                print "Directory Error: ,", e.output
        return f(*args, **kwargs)

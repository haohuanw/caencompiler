#!/usr/bin/env python
# -*- coding: utf-8 -*-
from caencompiler.modes.uploadmode import UploadMode
from fabric.api import *
from fabric.context_managers import *

def uploadTest(name, execution, subfolder, files, local, remote, host, user, passwords):
    u = UploadMode(name, execution, subfolder, files, local, remote)
    u.compile(host, user, passwords)

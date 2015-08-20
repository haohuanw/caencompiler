#!/usr/bin/env python
# -*- coding: utf-8 -*-
from caencompiler.modes.uploadmode import UploadMode
from caencompiler.modes.gitmode import GitMode
from caencompiler.modes.initmode import InitMode

def uploadTest(name, execution, subfolder, files, local, remote, host, user, passwords):
    u = UploadMode(name, execution, subfolder, files, local, remote)
    u.compile(host, user, passwords)

def GitTest(name, execution, subfolder, local, remote, host, user, passwords):
    g = GitMode(name, execution, subfolder, local, remote)
    g.compile(host, user, passwords)

def InitTest(gitAddr, remote, host, user, passwords):
    i = InitMode(gitAddr, remote)
    i.compile(host, user, passwords)

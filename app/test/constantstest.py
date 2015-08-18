#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from app.models.gitcommands import *
from fabric.api import *
from fabric.context_managers import *

def constantsremotetest():
    with settings(host_string = host):
        #with quiet():
        print GitRemoteCommands.test()
        print GitRemoteCommands.test()
        GitLocalCommands.test()

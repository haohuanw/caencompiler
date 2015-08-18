#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import * 

def getCaenDirect():
    run("pwd")

host = 'login.engin.umich.edu'
user = 'haohuanw'
passwords = '890922hH!@#'
PROJECT_LOCAL_PATH = os.getcwd()
CAEN_USER_DIRECTORY = "/afs/umich.edu/user/h/a/haohuanw/" 
PROJECT_REMOTE_PATH_GIT = CAEN_USER_DIRECTORY+"Documents/eecs482/git/"
PROJECT_REMOTE_PATH_UPLOADS = CAEN_USER_DIRECTORY+"Documents/eecs482/uploads/"

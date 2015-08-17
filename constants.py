#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from fabric.api import env

PROJECT_LOCAL_PATH = os.getcwd()
PROJECT_REMOTE_PATH = "Documents/eecs482/"
env.hosts = ['login.engin.umich.edu']

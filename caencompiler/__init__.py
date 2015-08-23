#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from caencompiler.args import Args
from caencompiler.utils.pathUtils import makeGoodPath
from caencompiler.modes.uploadmode import UploadMode
from caencompiler.modes.gitmode import GitMode
from caencompiler.modes.initmode import InitMode

def main():
    try:
        stream = file('config.yaml', 'r')
        config = yaml.load(stream)
    except:
        print "Cannot Open file"
        raise
    parser = Args()
    remotePath = makeGoodPath(config["PROJECT_REMOTE_PATH"])
    localPath = makeGoodPath(config["PROJECT_LOCAL_PATH"])
    if parser.args['init']:
        if parser.args['gitload']:
            i = InitMode(config["GITHUB_ADDR"], localPath, remotePath) 
            i.compile(config["HOST"], config["USER"], config["PASSWORDS"], True, parser.args['--verbose'])
        elif parser.args['upload']:
            i = InitMode(config["GITHUB_ADDR"], localPath, remotePath) 
            i.compile(config["HOST"], config["USER"], config["PASSWORDS"], False, parser.args['--verbose'])
    elif parser.args['gitload']:
        if len(config["GITHUB_ADDR"]) > 0:
            g = GitMode(parser.args["<name>"], parser.args["--exe"], parser.args["<subfolder>"], \
            localPath, remotePath)
            g.compile(config["HOST"], config["USER"], config["PASSWORDS"], parser.args['--verbose'])
        else:
            print "Github address is not provided."
            raise
    elif parser.args['upload']:
        u = UploadMode(parser.args["<name>"], parser.args["--exe"], parser.args["<subfolder>"], \
            parser.args['<file>'], localPath, remotePath)
        u.compile(config["HOST"], config["USER"], config["PASSWORDS"], parser.args['--verbose'])


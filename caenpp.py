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
    if parser.args['init']:
        i = InitMode(config["GITHUB_ADDR"], config["PROJECT_REMOTE_PATH"]) 
        i.compile(config["HOST"], config["USER"], config["PASSWORDS"])
    elif parser.args['gitload']:
        g = GitMode(parser.args["<name>"], parser.args["--exe"], parser.args["<subfolder>"], \
            config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH"]+"git/")
        g.compile(config["HOST"], config["USER"], config["PASSWORDS"])
    elif parser.args['upload']:
        u = UploadMode(parser.args["<name>"], parser.args["--exe"], parser.args["<subfolder>"], \
            parser.args['<file>'], config["PROJECT_LOCAL_PATH"], config["PROJECT_REMOTE_PATH"]+"uploads/")
        u.compile(config["HOST"], config["USER"], config["PASSWORDS"])

 

if __name__ == "__main__":
    main()

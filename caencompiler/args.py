#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docopt import docopt

class Args:

    def __init__(self):
        self.docs = """
CAENCOMPILE
            
Usage:
caenpp gitload [options] <name> [<subfolder>] [--exe=<execution>]
caenpp upload [options] <name> [<subfolder>] [--exe=<execution>] [<file>...]
caenpp init [options] (gitload|upload)
caenpp -h | --help

Options:
-h --help               Show this screen.
-v --verbose            Show detailed ssh commands.
--version               Show current version.
--exe=<execution>       Args for <name> program.
        """

        self.args = docopt(self.docs, version='CAENCOMPILER 1.0')


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docopt import docopt

class Args:

    def __init__(self):
        self.docs = """
CAENCOMPILE
            
Usage:
caencompile.py gitrun [options] <name> [--exe=<execution>]
caencompile.py uploadrun [options] <name> [--exe=<execution>] [<file>...]
caencompile.py -h | --help

Options:
-h --help               Show this screen.
-v --verbose            Show detailed ssh commands.
--version               Show current version.
--exe=<execution>       Args for <name> program.
        """

        self.args = docopt(self.docs, version='CAENCOMPILE 1.0')


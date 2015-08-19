#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.args import Args

def main():
    parser = Args()
    print parser.args

if __name__ == "__main__":
    main()

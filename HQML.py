#!/usr/bin/python3
import argparse

def dir_path(string):
    import os
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def build_argparser():
    parser = argparse.ArgumentParser(prog="hqml")
    subparsers = parser.add_subparsers(dest='function', help='help for subcommand')
    # create the parser for the "command_1" command
    parser_a = subparsers.add_parser('create', help='create project')
    parser_a.add_argument('path', help='target path')

    # create the parser for the "command_2" command
    parser_b = subparsers.add_parser('build', help='build project')

    

    return parser

if __name__ == '__main__':
    import sys
    parser = build_argparser()

    if len(sys.argv) == 1:
        parser.print_usage()

    args = parser.parse_args()

    if args.function == 'create':
        from create_project import create_project
        create_project(args.path)

    if args.function == 'build':
        from build_project import build_project
        build_project()
    
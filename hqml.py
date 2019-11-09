#!/usr/bin/python3
import argparse

def dir_path(string):
    import os
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def build_argparser():
    parser = argparse.ArgumentParser(prog="hqml")
    subparsers = parser.add_subparsers(dest='function', help='help for subcommand')
    # create the parser for the "command_1" command
    parser_a = subparsers.add_parser('create', help='create project')
    parser_a.add_argument('path', help='target path')

    # create the parser for the "command_2" command
    parser_b = subparsers.add_parser('build', help='build project')

    parser_c = subparsers.add_parser('config', help='configure project settings')
    parser_c.add_argument('--hot-reload', type=str2bool, help='hot reload')

    parser_d = subparsers.add_parser('update', help='update hqml')

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

    if args.function == "config":
        if args.hot_reload != None:
            print(args.hot_reload)
        else:
            print('Nothing to configure')

    if args.function == 'update':
        import subprocess, os
        toolchain_path = os.path.dirname(__file__)
        subprocess.call(['git', 'pull'], cwd=toolchain_path)
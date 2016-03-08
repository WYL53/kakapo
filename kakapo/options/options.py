# coding=utf-8
# author: veficos
# time: 2016-02-23

import argparse


def parser_options():
    options = [
        ['-c', '--config', {'type': str, 'help': 'set configuration file (default: winpot.conf)', 'default': 'winpot.conf'}],
        ['-v', '--version', {'action': 'store_true', 'help': 'show version and exit'}],
        ['-d', '--daemon', {'action': 'store_true', 'help': 'running by daemon (only Linux)'}],
    ]

    parser = argparse.ArgumentParser()

    for arg in options:
        parser.add_argument(arg[0], arg[1],  **arg[2])

    args = parser.parse_args()

    for key in args.__dict__:
        globals()[key] = args.__dict__[key]

parser_options()

del parser_options

# coding=utf-8

# author: veficos
# time: 2016-02-23

import ConfigParser
import os
import sys


def get_config(options):
    if not os.path.exists(options.config):
        sys.stderr.write("Can't open %s file" % options.config)
        sys.exit(0)

    conf = ConfigParser.RawConfigParser()
    conf.read(options.config)

    return conf

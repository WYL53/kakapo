# coding=utf-8

# author: veficos
# time: 2016-02-23

import logging
import os

import logging.handlers


def get_logger(conf, daemon):
    path = conf.get('Logging', 'Path')
    name = conf.get('Logging', 'Name')
    devel = conf.get('Logging', 'Devel')
    formatter = conf.get('Logging', 'Formatter')
    maxBytes = eval(conf.get('Logging', 'MaxBytes'))
    backupCount = eval(conf.get('Logging', 'BackupCount'))

    if not os.path.exists(path):
        os.mkdir(path)

    formatter = logging.Formatter(formatter)

    fh = logging.handlers.RotatingFileHandler(os.path.join(path, name), maxBytes=maxBytes, backupCount=backupCount)
    fh.setFormatter(formatter)

    logger = logging.getLogger("winpot")
    logger.setLevel(getattr(logging, devel))
    logger.addHandler(fh)

    if not daemon:
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        sh.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        logger.addHandler(sh)

    return logger

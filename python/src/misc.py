# -*- coding: utf-8 -*-
"""
Misc functions

Created on Sun Feb  4 09:48:50 2018

@author: pi
"""

import logging
import datetime as dt


def log_version():
    ''' Log the version and hash from git repo in log file. To be called
    at the setup of a new run.
    '''
    import subprocess
    import os
    try:
#        os.chdir('/Users/joncosgrove/Dropbox/Projects/GPS_robot/megatron')
        ver_tag = subprocess.check_output(["git", "describe"]).strip()
        ver_hash = subprocess.check_output(["git", "rev-parse", "--short",
                                            'HEAD']).strip()
        logging.info('VERSION TAG: ' + str(ver_tag))
        logging.info('VERSION HASH: ' + str(ver_hash))
        return
    except Exception as exception:
        if type(exception).__name__ is 'CalledProcessError':
            logging.error('Git version info not avaliable')
        return


def configure_logging(path='/home/pi/megatron/python/Log', filemode='w',
                      level=logging.DEBUG):
    '''Setup logging given a path and event serverity level

    Parameters
    ----------
    path = string
    path to log file directory

    level = logging event severity threshold

    Return
    ------
    n/a
    '''

    filename = 'Log_' + dt.datetime.now().strftime('%Y%m%d_%H%M%S%p') \
               + '.log'
    print(filename)
    logging.basicConfig(filename=filename, level=level)
    logging.info('Begin')


if __name__ == "__main__":
    import doctest
    doctest.testmod()

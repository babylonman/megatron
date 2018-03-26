# -*- coding: utf-8 -*-
"""
Misc functions

Created on Sun Feb  4 09:48:50 2018

@author: pi
"""

import logging
import datetime as dt


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

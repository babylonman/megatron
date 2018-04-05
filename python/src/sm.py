#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:03:30 2018

@author: joncosgrove
"""

from statemachine import StateMachine, State
import logging

class Machine(StateMachine):
    '''State machine definition for overall operation
    
    '''
    
#    define states
    init = State('init', initial=True)
    operate = State('operate')
    shutdown = State('shutdown')
    off = State('off')

#    define transitions
    stop = operate.to(shutdown) | init.to(shutdown)
    run = init.to(operate)
    power_off = shutdown.to(off)
    start = shutdown.to(init) | off.to(init)

#    define transition actions
    def on_enter_shutdown(self):
        logger.info('entered shutdown state')
        pass

    def on_enter_operate(self):
        pass

    def on_enter_off(self):
        pass

    def on_enter_init(self):
        pass

    def on_exit_shutdown(self):
        pass

    def on_exit_operate(self):
        pass

    def on_exit_off(self):
        pass

    def on_exit_init(self):
        pass


logger = logging.getLogger(__name__)

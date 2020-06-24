# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:55:54 2020

@author: Gokhale
"""

import logging
logging.basicConfig(level=logging.WARNING,force=True)
log=logging.getLogger(__name__)

if __name__ == '__main__':
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical message')

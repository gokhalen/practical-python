# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:21:12 2020

@author: Gokhale
"""
import logging
log = logging.getLogger(__name__)

def split(line,types,delimiter):
    line=line.split(delimiter)
    output=[ func(val) for func,val in zip(types,line)]
    return output   

def parse(f,types=None,names=None,delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,delimiter))
        except ValueError as e:
            log.warning("Couldn't parse: %s", line)
            log.debug("Reason: %s",e)
    return records
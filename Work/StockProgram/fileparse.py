# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:48:50 2020

@author: Gokhale
"""

import csv
import sys

def parse_csv(filename:str,select:list=None,
              types=[],has_headers=True,delimiter=",",silence_errors=False):
    '''
    Parse a CSV file into a list of records
    filename: file to be opened
    select:  list of fields to be selected
    Notes: types defaults to empty list. Do NOT mutate it (Amy Hanlon's talk)
    '''
    try:
       if (has_headers==False) and (select != None):
            raise RuntimeError("Select argument requires col headers")
    except RuntimeError as e:
       raise
       
    with open(filename) as f:
        rows    = csv.reader(f,delimiter=delimiter)
        records = []        

        if has_headers:
            
            assert(select !=None),'Need to specify fields to select'
            
            #if types are specified for conversion, then they must be equal to number of fields        
            if types:
                assert (len(select) == len(types)), 'Length of select is not equal to length of types'

            # Read the file headers
            headers = next(rows)
        
            # check to see which of the user specified fields 
            # are actually found in the file
            foundfields= []
            foundtypes = []
        
            for ii,ss in enumerate(select):
                if ss not in headers:
                    print(f'User specified field {ss} not found in {filename}')
                    sys.stdout.flush()
                else:
                    foundfields.append(ss)
                    if types:
                        foundtypes.append(types[ii])
                            
        # proceed if foundfields is not empty
            if foundfields:
                indices = [ headers.index(ff) for ff in foundfields ]
                for rowno,row in enumerate(rows):
                    # if blank row then skip to the next row
                    if not row:
                        continue
                # if types were specified, do conversion
                    if foundtypes:
                        try:
                # Note the numbers in row are strings
                # int('32.2') throws ValueError
                            record = { ff:tt(row[ii]) for ff,ii,tt in zip(foundfields,indices,foundtypes)}
                        except ValueError as e:
                            record = {}
                            if not silence_errors: print(f'Bad data in {filename} on line {rowno+2}')
                            
                    else:   
                        record = { ff:row[ii] for ff,ii in zip(foundfields,indices) }
                    # do not append blank records
                    if record: records.append(record)
            else:
                if not silence_errors: print(f'No user specified fields could be found in {filename}')
                sys.stdout.flush()
        else:
             # case of no headers
             for row in rows:
                 if not row:
                     continue
                 record =(row[0],float(row[1]))
                 records.append(record)
    
    return records
        
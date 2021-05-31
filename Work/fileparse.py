# fileparse.py
#
# Exercise 3.8

import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter = ','):
    '''
    Parse a CSV file into a list of records
    '''
    
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices ]

            #Check if types are given or not and parse the value according to that
            
            if types:
                row = [func(val) for func, val in zip(types, row)]
            
            #Check if headers are given or not and calculate according to that    
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            
            records.append(record)
        print(records)
    return records

portfolio = parse_csv('Data/prices.csv', select=['name','price'], types=[str,float], has_headers=False, delimiter = ' ')



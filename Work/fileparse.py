# fileparse.py
#
# Exercise 3.9

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter = ','):
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
        for row_index, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices ]

            #Check if types are given or not and parse the value according to that
            
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {row_index}: Couldn't convert {row}")
                    print(f"Row {row_index}: Reason {e}")
                    continue
            
            #Check if headers are given or not and calculate according to that    
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            
            records.append(record)
        
    return records

portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
print(portfolio)




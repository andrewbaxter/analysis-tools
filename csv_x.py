#!/bin/python2

import sys, csv
csv.field_size_limit(sys.maxsize)

with open(sys.argv[1], 'r') as text:
    for item in csv.DictReader(text):
        out = []
        for tag in sys.argv[2:]:
            if tag in item:
                out.append(item[tag])
        print(' '.join(out))


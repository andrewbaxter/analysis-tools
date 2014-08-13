#!/bin/python2

import json, sys

with open(sys.argv[1], 'r') as text:
    items = json.loads(text.read().decode('utf-8'))

for item in items:
    out = []
    for key in sys.argv[2:]:
        if key in item:
            out.append(unicode(item[key]))
    print(u' '.join(out).encode('utf-8'))


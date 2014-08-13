#!/bin/python2
import sys, re

sys.argv.pop(0)

if sys.argv:
    f = open(sys.argv[-1], 'r')
    sys.argv.pop()
else:
    f = sys.stdin

regexes = [re.compile(pattern) for pattern in sys.argv]

for line in f:
    line = line.strip().rstrip()
    parts = []
    for regex in regexes:
        found = regex.search(line)
        if found:
            try:
                parts.append(found.group(1))
            except:
                parts.append(found.group())
            line = regex.sub('', line)
        else:
            break
    if parts:
        parts.append(line)
        print(' '.join(parts))


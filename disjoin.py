#!/bin/python2
import sys

sys.argv.pop(0)

dis = sys.argv.pop(0) == 'disjoin'

keys = {}
with open(sys.argv.pop(0), 'r') as f:
    for line in f:
        parts = [part for part in [part.strip().rstrip() for part in line.split(' ')] if part]
        key = parts.pop(0).strip().rstrip()
        keys[key] = parts

with open(sys.argv.pop(0), 'r') as f:
    for line in f:
        parts = [part for part in [part.strip().rstrip() for part in line.split(' ')] if part]
        key = parts.pop(0).strip().rstrip()
        original = keys.get(key)
        if not dis and original:
            print(' '.join([key] + original + parts))
        elif dis and not original:
            print line


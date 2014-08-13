#!/bin/python2

import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

previous = ''
for line in sys.stdin:
    for index, char in enumerate(line):
        if char == ' ' or char == '\n' or index >= len(previous) or previous[index] != char:
            sys.stdout.write(char)
        else:
            sys.stdout.write(bcolors.OKBLUE + char + bcolors.ENDC)
    previous = line


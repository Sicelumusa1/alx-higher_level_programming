#!/usr/bin/python3
import sys
a = len(sys.argv)
for i in range(0, a):
    if i == 0:
        print("{} arguments.".format(i))
    else:
        print("{} arguments:".format(a))
        print("{}: {}".format(i, sys.argv[i]))

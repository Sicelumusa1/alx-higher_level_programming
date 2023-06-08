#!/usr/bin/python3
import sys
a = len(sys.argv)
if __name__ == "__main__":
    num = 0
    _sum = 0
    for i in range(1, a):
        num = int(sys.argv[i])
        _sum += num
    print(_sum)


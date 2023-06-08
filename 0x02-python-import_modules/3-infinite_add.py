#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = len(sys.argv)
    num = 0
    _sum = 0
    for i in range(1, a):
        num = int(sys.argv[i])
        _sum += num
    print(_sum)

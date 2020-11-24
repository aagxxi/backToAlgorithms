#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    r = [0]*len(a)
    if len(a)==d: return a
    if len(a)<d: d= d % len(a)
    for x in range( len(a)-1, -1, -1 ):
        i = x - d
        if i<0: i=i+len(a)
        r[i] = a[x]
    return r

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


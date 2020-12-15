#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):

    st = scores[0]
    ct = 0
    sb = scores[0]
    cb = 0
    for x in range( 1, len(scores) ):
        if scores[x]>st:
            st = scores[x]
            ct += 1
        elif scores[x]<sb:
            sb = scores[x]
            cb += 1
    
    return [ ct, cb ]


if __name__ == '__main__':

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


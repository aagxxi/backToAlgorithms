#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    pos = 0
    mpo = 0
    mxh = ar[mpo]

    while len(ar)>pos:
        if ar[pos]>=mxh:
            mxh=ar[pos]
            mpo=pos
        pos=pos+1
    
    qty=1
    pos=mpo-1
    while pos>=0:
        if ar[pos]==mxh:
            qty=qty+1
        pos=pos-1

    return qty

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


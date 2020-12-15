#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    i = 0
    s = 0
    while ( i < len(arr) ):
        if arr[i] == i+1:
            i=i+1
        else:
            p = arr[i]-1
            arr[i] = arr[p]
            arr[p] = p+1
            s = s+1
    return s

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

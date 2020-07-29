#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):

    def best( n ):  # greedy algorithm
        r5 = n // 5
        r2 = ( n - ( r5 * 5 ) ) // 2
        r1 = n - ( ( r5 * 5 ) + ( r2 * 2 ) )
        return [ r5, r2, r1 ]

    if len( arr )<2:
        return 0

    arr.sort()

    ops = 1000 * len(arr)
    for y in range( 0, 5 ):  # 0-4 decrement first element  
        stps = 0 if y==0 else 1
        for x in range( 1, len( arr ) ):  # can we go into negatives with bigger y's?
#            count( x, 0 if y==0 or bst[0][0] )
            ds = best( arr[x]-(arr[0]-y) )
            stps = stps + ( ds[0] + ds[1] + ds[2] )
#            if ( ds[0] + ds[1] + ds[0] )<=6: print( "stps:{} ds:{} ops:{} y:{}".format( stps, ds, ops, y) )
        if stps<ops: ops= stps

    return ops


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


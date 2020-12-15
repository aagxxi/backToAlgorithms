#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    def need_at( x ):
        if q[x] == (x+1):
            return 0
        if q[x-1] == (x+1):
            q[x-1] = q[x]
            q[x] = x
            return 1
        if q[x-2] == (x+1):
            q[x-2] = q[x-1]
            q[x-1] = q[x]
            q[x] = x
            return 2
        return -1

    b = 0
    for x in range( len(q)-1, 0, -1 ):
#        print( "x={}".format( x ) )
        j = need_at( x )
        if j<0:
            print( "Too chaotic" )
            return
        b = b + j
    print( "{}".format( b ) )

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):

    if len(s) < m:
        return 0
#    print( " we are going to do it m={}".format( m ))
    ss = 0
    cc = 0
    for x in range( 0, min( m, len(s) ) ):
        ss += s[ x ]
#    print( " ss={}".format( ss ))
    if ss==d:
        cc += 1
    for x in range( 1, len( s )-m+1 ):
        ss = ss + s[ x+m-1 ] - s[ x-1 ]
#        print( "loop ss={} x+m={} x-1={}".format( ss, x+m, x-1 ))
        if ss==d:
            cc += 1

    return cc

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()


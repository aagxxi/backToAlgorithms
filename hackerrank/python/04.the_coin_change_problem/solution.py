#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here

    cache = {}
    c.sort( reverse=True )

#    print( "n={} c={}".format(n,c))

    def add_coin( p, v, s ): # p= pointer to c (coin to add)  v= value total   return: total solutions so far

        t = c[p]

        if (v+t)>n:
#            print( "max value = {}".format( s, c[p] ))
            return 0

        if (v+t)==n:
#            print( "found {} {}".format( s, c[p] ))
            return 1

        r = 0
        for x in range( p, len(c) ):
            if ( x, v+t ) in cache.keys():
                r = r + cache[ ( x, v+t ) ]
#                print( "cache {}/{}".format( x, v+t ) )
            else:
                toc = add_coin( x, v+t, "{} {}".format( s, c[p] ) )
                cache[ ( x, v+t ) ] = toc
                r = r + add_coin( x, v+t, "{} {}".format( s, c[p] ) )

        return r

    rr = 0
    for x in range( 0, len(c) ):
        rr = rr + add_coin( x, 0, "" )

    return rr


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

re = [ 0, 1, 1, 1, 2, 3 ] + [None] * 40  # we know the first five
pr = { 1:0, 2:1, 3:2, 4:2 }
# Complete the redJohn function below.
def redJohn(n):

    def sols4n( n ):
        if re[n]: # dont need to check if n<5 because preloaded
#            print( "cache n={} r={}".format( n, re[n] ) )    
            return re[n]
        r = sols4n( n-1 ) + sols4n( n-4 )
        re[n] = r
#        print( "sols4n n={} r={}".format( n, r ) )
        return r

    def primes( n ):
        if n in pr:
            return pr[n]
        qyp = 0
        isp = [False,False] + [True] * n
        for x in range( 2,n+1 ):
            if isp[x]:
                qyp += 1
                if ( x*x )<=n:
                    for j in range( x*x, n+1, x ):
                        isp[ j ] = False
        pr[ n ] = qyp
        return qyp

    seg = sols4n( n )
#    print( "solutions for {}: {}".format( n, seg ) )

    p = primes( seg )

#    print( "primes for {}: {}".format( seg, p ) )

    return p


if __name__ == '__main__':

#    for x in range(1,12):
#        redJohn( x )
#    exit()

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()


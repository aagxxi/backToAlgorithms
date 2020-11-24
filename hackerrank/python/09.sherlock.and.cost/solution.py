#!/bin/python3

# import math
import os
# import random
# import re
import sys


# Complete the cost function below.
def cost(B):

    odd = 0
    even = 0

# MY SOLUTION
    for i in range(1, len(B)):
        nodd = even+(B[i]-1)
        if odd > nodd:
            nodd = odd
        neven = odd+(B[i-1]-1)
        if even > neven:
            neven = even
        odd = nodd
        even = neven

# MINIMAL SOLUTION
#        nodd = max(odd, even+(B[i]-1))
#        even = max(even, odd+(B[i-1]-1))
#        odd = nodd

# EDITORIALIZED SOLUTION
#        pp = B[i-1] - 1
#        tt = B[i] - 1

#        o_n = max(odd, even+pp )
#        e_n = max(even, odd+tt )

#        odd = o_n
#        even = e_n

# FIRST WRONG SOLUTION
#        if (i % 2) == 0:
#            even = even + abs( B[i-1] - 1 )
#            odd = odd + abs( 1 - B[i] )
#        else:
#            even = even + abs( 1 - B[i] )
#            odd = odd + abs( B[i-1] - 1 )

    #print( "odd:{} even:{}".format(odd,even))

    if odd > even:
        return odd
    else:
        return even


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()

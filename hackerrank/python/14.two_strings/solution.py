#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    used = [ False ] * ( ord('z')-ord('a')+1 )

    for c in s1:
        used[ ord(c)-ord('a') ] = True
    for c in s2:
        if used[ ord(c)-ord('a') ]:
            return "YES"
    return "NO"

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

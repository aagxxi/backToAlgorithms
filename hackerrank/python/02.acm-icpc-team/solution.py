#!/bin/python3

# time bash -c "cat bigexample | python3 ./solution.py"
# 412
# 1

# real	0m11.084s
# user	0m11.081s
# sys	0m0.003s


import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):

    def sharedtopics( at1, at2 ):

        s = 0
        x = 0
        while x<len(at1):
            if at1[x]=='1' or at2[x]=='1':
                s = s + 1
            x = x + 1

        return s
    
    def sharetopics( at1, at2 ):
        st = at1 | at2
        r = 0
        while (st): 
            st &= (st-1)  
            r= r+1
        return r

    teams = [0] * 500
    binar = [None] * 500

    m = 0
    i = 0
    while i<(len(topic)-1):
        j = i+1
        while j<len(topic):
            if binar[i]==None: binar[i]=int( topic[i], 2 )
            if binar[j]==None: binar[j]=int( topic[j], 2 )
#            t = sharedtopics( topic[i], topic[j] )
            tt = sharetopics( binar[i], binar[j] )
#            if tt!=t:
#                print( "t={} tt={}".format(t,tt))
            if tt>m:
                m=tt
            teams[tt]=teams[tt]+1
            j = j+1
        i = i+1

    return [ m, teams[m] ]

if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout    

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

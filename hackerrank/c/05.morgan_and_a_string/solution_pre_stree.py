#!/bin/python3

import math
import os
import random
import re
import sys

test=''

# Complete the morganAndString function below.
def morganAndString(a, b):

    r = ''
    la = len(a)
    lb = len(b)
    pa = 0
    pb = 0
    dp = {}

    def top(aa, bb, above):
#        na = a[aa] if aa<la else ( "|" if above else "0" )
#        nb = b[bb] if bb<lb else ( "|" if above else "0" )
        na = a[aa] if aa<la else "|"
        nb = b[bb] if bb<lb else "|"
        return ( na, nb )

    def untie(aa, bb):
        tie = True
        lst = a[aa]
        equ = True
        qequ = 0
        lequ = 0
        abo = True
        qabo = 0
        pp = aa
        dpi = aa-bb
        if dpi in dp:
            if dp[ dpi ][0] < aa:
                ( na, nb )=top( dp[dpi][0], dp[dpi][1], False )
#                print( "hit ({}) [{}]{}<>{}[{}]".format( dpi, dp[dpi][0], na, nb,dp[dpi][1] ) )
                return ( na<nb, 1 )
        while tie:
            ( na, nb )=top( aa, bb, False )
            if ( na==nb and na!='|' and nb!='|' ):
#                if aa>65000: print( 'por aca' )
#                if ( pp<aa ):
#                    ( la, lb )=top( aa-1, bb-1, False )
#                    if ( la==na ):
#                        lequ += 1
#                    else:
#                        lequ = 1
#                    if aa>65000: print( "untie aa={} bb={} lst={}, na={} nb={} la={} lb={} lequ={}".format( aa, bb , lst, na, nb , la, lb, lequ ))                
                aa+=1
                bb+=1
                if equ:
                    if lst!=na:
                        equ=False
                    else:
                        qequ+=1
                if abo:
                    if ord(lst)<=ord(na):  # <= slow, works  < fast, does not work
                        abo=False
                    else:
                        qabo+=1
            else:
                tie=False
#        qequ=1
#        qabo=qabo-4
#        print( "untie aa={} bb={} qequ={} qabo={}".format( aa, bb , qequ, qabo ))
#        print( "untie aa={} bb={} qequ={} qabo={} lequ={}".format( aa, bb , qequ, qabo, lequ ))

        dp[ dpi ]=[ aa, bb ]

        return ( na<nb, qequ if qequ>qabo else qabo )
#        return ( na<nb, qabo )

    while(( pa<la )or( pb<lb )):
#        na = a[pa] if pa<la else "|"
#        nb = b[pb] if pb<lb else "|"
        ( na, nb )=top( pa, pb, True )
#        print( "a[pa]={} b[pb]={} pa={} pb={}".format( na, nb, pa, pb))
#        print( "a[pa:]={} b[pb:]={} pa={} pb={} r={}".format( a[pa:], b[pb:], pa, pb, r))
        if( ord(na)==ord(nb) ):
            ( un, jm )=untie( pa,pb )
#            if jm: print( "untie by {} {}".format( "a" if un else "b", jm ))
            if un:
                for x in range(jm):
                    r=r+a[pa]
                    pa+=1
            else:
                for x in range(jm):
                    r=r+b[pb]
                    pb+=1
        elif( ord(na)<ord(nb) ):
#            print( "<a pa={} na={} nb={}".format(pa,na,nb))
            r=r+a[pa]
            pa+=1
        elif ( ord(na)>ord(nb) ):
#            print( ">b pb={} na={} nb={}".format(pb,na,nb))
            r=r+b[pb]
            pb+=1

#        if( False and ( test[0:len(r)]!=r )):
#            print( "error len(r)={} pa={} pb={} la={} lb={}".format( len(r), pa, pb, la, lb) )
#            print( "r=..." + r[len(r)-10:len(r)] )
#            print( "t=..." + test[len(r)-10:len(r)])
#            exit()
        

    return r


if __name__ == '__main__':

#    print( "1" )
#    print( "{}{}".format( "O"*94999, "Z" ))
#    print( "{}{}".format( "O"*94999, "Y" ))
#    exit()

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except:
        fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()

# Suffix Tree:
#   https://en.wikipedia.org/wiki/Suffix_tree
# Suffix Array:
#   https://en.wikipedia.org/wiki/Suffix_array

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    
    def rotate( mtx,m,n,r ):

#        print ( "asked to rotate {}x{}, {} times".format( m,n,r ) )

        if( m>2 and n>2 ):
            rotate( mtx, m-2, n-2, r )

        perimeter = ((m-1)*2)+((n-1)*2)
        by = ( ( len( mtx ) - m ) // 2 ) + m
        bx = ( ( len( mtx[0] ) - n ) // 2 ) + n
        ty = by - m + 1
        tx = bx - n + 1
        if r>perimeter:
            times = perimeter - (r % perimeter)
        else:
            times = perimeter - r

#        print( "will rotate {}x{} @ {}x{}=>{}x{}, {} times (perimeter={})".format( m,n,ty,tx,by,bx,times,perimeter ) )

        linear = [None] * perimeter

        for x in range( tx, bx+1 ):
            tp = (x-tx+times-perimeter) if (x-tx+times)>=perimeter else (x-tx+times)
            bp = (((perimeter // 2)+(n-1)+times-(x-tx))-perimeter) if ((perimeter // 2)+(n-1)+times-(x-tx))>=perimeter else ((perimeter // 2)+(n-1)+times-(x-tx))
#            print( "({},{})=>{} / ({},{})=>{}".format( ty, x, tp, by, x, bp ) )
            linear[ tp ] = mtx[ ty-1 ][ x-1 ]
            linear[ bp ] = mtx[ by-1 ][ x-1 ]
        for y in range( ty+1, by ):
            fp = (n-1)+(y-ty)+times-perimeter if ((n-1)+(y-ty)+times)>=perimeter else (n-1)+(y-ty)+times
            lp = (((perimeter // 2)+(n-1)+(m-1)+times-(y-ty))-perimeter) if ((perimeter // 2)+(n-1)+(m-1)+times-(y-ty))>=perimeter else ((perimeter // 2)+(n-1)+(m-1)+times-(y-ty))
#            print( "({},{})=>{} / ({},{})=>{}".format( y, bx, fp, y, tx, lp ) )
            linear[ fp ] = mtx[ y-1 ][ bx-1 ]
            linear[ lp ] = mtx[ y-1 ][ tx-1 ]

#        print( "mtx={}".format( mtx ))
#        print( "linear={}".format( linear ))

        for x in range( 0,perimeter ):
            if( x<n ):
                ( yy,xx )=( ty-1,x+tx-1 )
            elif ( x<(n+m-1) ):
                ( yy,xx )=( ty+(x-n),bx-1 )
            elif ( x<(n+m+n-2) ):
                ( yy,xx )=( by-1,bx-(x-(n+m-3)) )
            else:
                ( yy,xx )=( by-(x-(n+m+n-4)),tx-1 )
            mtx[ yy ][ xx ] = linear[ x ]

#        print( "mtx={}".format( mtx ))

    m = len( matrix )
    n = len( matrix[0] )
    rotate( matrix, m, n, r )

    for y in range( len( matrix )):
        s = ""
        for x in range( len( matrix[0] )):
            s = "{} {}".format( s, matrix[y][x] )
        print( s.strip() )


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

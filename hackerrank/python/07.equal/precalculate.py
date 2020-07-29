#!/bin/python3


def precalculate( n, gree ):

    dee = 1000
    det = [ 0, 0, 0 ]

    def add( r, d, t ):
        nonlocal dee, det, gree
        v = t[0] * 5 + t[1] * 2 + t[2] * 1
#        print( "r={} d={} t={} v={}".format(r,d,t,v))
        if r==0:
            if d<dee:
                det = t
                dee = d
            return
        if r<gree:
            if r>=5:
                add( r-5, d+1, [ t[0]+1, t[1], t[2] ] )
            if r>=2:
                add( r-2, d+1, [ t[0], t[1]+1, t[2] ] )
            if r>=1:
                add( r-1, d+1, [ t[0], t[1], t[2]+1 ] )
        else:
            add( r-5, d+1, [ t[0]+1, t[1], t[2] ] )
        return

    add( n, 0, [ 0, 0, 0 ] )

    return ( dee, det )

def best( n ):
    r5 = n // 5
    r2 = ( n - ( r5 * 5 ) ) // 2
    r1 = n - ( ( r5 * 5 ) + ( r2 * 2 ) )
    return [ r5, r2, r1 ]    

if __name__=="__main__":

    for x in range( 1000, 0, -1):
        ( r1, t1 ) = precalculate( x, 10 )
        ( r2, t2 ) = precalculate( x, 20 )
        ( r3, t3 ) = precalculate( x, 5 )
        t = best( x )
        t4 = t
        r4 = t[0] + t[1] + t[2]
        if( r1!=r2 )or( r2!=r3 )or( r3!=r4 ):
            print( "different r1={} r2={} r3={} r4={}".format( r1,r2,r3,r4 ) )
            print( "          t1={} t2={} t3={} t4={}".format( t1,t2,t3,t4 ))
            exit()
        print( "n={}, r={}".format( x, ( r1, t ) ) )
#!/bin/python3

# import math
# import os
# import random
# import re
import sys
from functools import lru_cache
# import STree     # https://github.com/ptrus/suffix-trees
# from suffixtree import Tree    # https://github.com/cceh/suffix-tree
# https://codeforces.com/blog/entry/74540
# https://github.com/chenzhiw/generalized-suffix-tree-python
# no probado: https://github.com/abahgat/suffixtree

# #########################################################################################


class STree( object ):

    def make_node( self, _pos, _len):
        # global s, n, sz, to, link, fpos, slen, pos, node
        self.fpos[ self.sz ] = _pos
        self.slen[ self.sz ] = _len
        self.sz += 1
        return self.sz-1

    def go_edge( self ):
        # global s, n, sz, to, link, fpos, slen, pos, node
        while ( self.pos > self.slen[ self.to[ self.node].get( self.s[ self.n - self.pos ], 0 ) ] ):
            self.node = self.to[ self.node ].get( self.s[ self.n - self.pos ], 0 )
            self.pos -= self.slen[ self.node ]

    def add_letter( self, c ):
        # global s, n, sz, to, link, fpos, slen, pos, node
        self.s[ self.n ] = c
        self.n += 1
        self.pos += 1
        last = 0
        while( self.pos > 0 ):
            self.go_edge()
            edge = self.s[ self.n - self.pos ]
            v = self.to[ self.node ].get (edge, 0 )
            t = self.s[ self.fpos[ v ] + self.pos - 1 ]
            if ( v == 0 ):
                self.to[ self.node ][ edge ] = self.make_node( self.n - self.pos, self.inf )
                self.link[ last ] = self.node
                last = 0
            elif ( t == c ):
                self.link[ last ] = self.node
                return
            else:
                u = self.make_node( self.fpos[v], self.pos - 1 )
                self.to[u][c] = self.make_node( self.n - 1, self.inf )
                self.to[u][t] = v
                self.fpos[v] += self.pos - 1
                self.slen[v] -= self.pos - 1
                self.to[ self.node ][ edge ] = u
                self.link[ last ] = u
                last = u
            if( self.node == 0 ):
                self.pos -= 1
            else:
                self.node = self.link[ self.node ]

    def init_tree( self, st ):
        # global slen, ans, inf, maxn, s, to, fpos, slen, link, node, pos, sz, n
        #
        self.text = st
        self.len_text = len( st )
        #
        self.inf = int( 1e9 )
        maxn = len( st )*2+1 #int(1e6+1)
        self.s = [0]*maxn
        self.to = [ {} for i in range( maxn ) ]
        self.fpos, self.slen, self.link = [0]*maxn, [0]*maxn, [0]*maxn
        self.node, self.pos = 0, 0
        self.sz = 1
        self.n = 0
        self.slen[ 0 ] = self.inf
        self.ans = 0
        for c in st:
            self.add_letter( ord( c ) )

    def traverse_edge( self, st, idx, start, end ):
        # global len_text, len_st
        k = start
        # while k <= end and k < self.len_text and idx < self.len_st:
        while k <= end and k < self.len_text and idx < len( st ):
            if self.text[k] != st[idx]:
                return -1
            k += 1
            idx += 1
        # if idx == self.len_st:
        if idx == len( st ):
            return idx
        return 0

    def edgelen( self, v, init, e ):
        if( v == 0 ):
            return 0
        return e-init+1

    @lru_cache( maxsize=10000001 )
    def traverse( self, v, st, idx ):
        # global len_st
        print( "traverse=[v={},st={},idx={}]".format( v, st, idx ) )
        r = -1
        init = self.fpos[ v ]
        end = self.fpos[ v ] + self.slen[ v ]
        e = end-1
        if v != 0:
            r = self.traverse_edge( st, idx, init, e )
            if r != 0:
                if r == -1:
                    return []
                return [ v, idx, init, end, e, r]  # return[ r ]
        idx = idx + self.edgelen( v, init, e )
        if idx > len( st ):    # self.len_st:
            return []
        k = ord( st[ idx ] )
        children = self.to[ v ]
        if k in children:
            vv = children.get( k, 0 )
            return self.traverse( vv, st, idx )
        return []

    @lru_cache( maxsize=1001*10 )
    def solve(T, query):
        traverse.cache_clear()
        return "y\n" if traverse(0, query, 0) else "n\n"

#def main():
#    global text, len_st, len_text
#    k = readint()
#    for ki in range(k):
#        text = read()+"$"
#        len_text = len(text)
#        init_tree(text)
#        q = readint()
#        for qi in range(q):
#            query = read()
#            len_st = len(query)
#            stdout.write(solve(text, query))

# #########################################################################################



# Complete the morganAndString function below.
def morganAndString(a, b):

#    st = STree.STree( [ a, b ] )
#    st = Tree ({ 'A' : a , 'B' : b })

    stree = STree()
    lens = ( len(a)+1, len(b)+1 )
    bigg = a+"$"+b+"#"
    stree.init_tree( bigg )

    print( "a={} len={}".format(a,len(a)) )
    print( "b={} len={}".format(b,len(b)) )
    print( "---" )

#    print( st.lcs() )
    print( stree.traverse( 0, "O", 0 ) )

    return ""


if __name__ == '__main__':

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

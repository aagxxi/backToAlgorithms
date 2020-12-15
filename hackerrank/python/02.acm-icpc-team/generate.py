
import random

for x in range( 500 ):
  y=random.getrandbits(499)
  print( "{0:0499b}".format(y) )
    

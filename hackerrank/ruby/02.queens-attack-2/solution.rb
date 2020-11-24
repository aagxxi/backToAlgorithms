#!/bin/ruby

require 'json'
require 'stringio'

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles)

    # recorrer los obstaculos
    # ver si el obstaculo esta dentro del tablero
    # igual columna o fila, es obstaculo para los verticales u orizontales
    # igual suma o resta respecto a la reina, es obstaculo para los diagonales
    # guardar los que mas cerca están y calcular.

    def diagcloser( q, p1, p2 )
        return ( q[0]-p1[0] ).abs < ( q[0]-p2[0] ).abs ? p1 : p2
    end

    def vertcloser( q, p1, p2 )
        return diagcloser( q, p1, p2 )
    end

    def horicloser( q, p1, p2 )
        return ( q[1]-p1[1] ).abs < ( q[1]-p2[1] ).abs ? p1 : p2
    end

    queen = [ r_q, c_q ]
    clobs = []
    clobs[0] = [r_q,0]                                             # horiz left
    clobs[1] = r_q>c_q ? [r_q-c_q,0] : [0,c_q-r_q]                 # diag up left
    clobs[2] = [0,c_q]                                             # vert up
    clobs[3] = (r_q-1)<(n-c_q) ? [0,c_q+r_q] : [r_q-(n-c_q)-1,n+1] # diag up right
    clobs[4] = [r_q,n+1]                                           # horiz right
    clobs[5] = r_q>c_q ? [n+1,n-(r_q-c_q)+1] : [n-(c_q-r_q)+1,n+1] # diag down right
    clobs[6] = [n+1,c_q]                                           # vert down
    clobs[7] = (r_q+c_q)<=n ? [r_q+c_q,0] : [n+1,c_q-(n-r_q)-1]    # diag down left
    
#    puts "pre"
#    p clobs

    obstacles.each { |obs| 
    
        if obs[0]>n or obs[1]>n             # ignore, out of board
#            puts "out of board [" + obs[0].to_s + "/" + obs[1].to_s + "]"
        elsif obs==queen # obs[0]==r_q and obs[1]==c_q   # ignore, position of the queen
#            puts "position of the queen [" + obs[0].to_s + "/" + obs[1].to_s + "]"
        elsif obs[1]==c_q                   # same column than queen
#            puts "same column than queen [" + obs[0].to_s + "/" + obs[1].to_s + "]"
            if obs[0]>r_q  # bottom
                clobs[6] = vertcloser( queen, obs, clobs[6] )
            else           # above
                clobs[2] = vertcloser( queen, obs, clobs[2] )
            end
        elsif obs[0]==r_q
#            puts "same row than queen [" + obs[0].to_s + "/" + obs[1].to_s + "]"
            if obs[1]>c_q  # right
                clobs[4] = horicloser( queen, obs, clobs[4] )
            else           # left
                clobs[0] = horicloser( queen, obs, clobs[0] )
            end
        elsif (obs[0]-r_q).abs == (obs[1]-c_q).abs
#            puts "diagonal to the queen [" + obs[0].to_s + "/" + obs[1].to_s + "]"
            if obs[0]<r_q and obs[1]<c_q
                clobs[1] = diagcloser( queen, obs, clobs[1] )
            elsif obs[0]<r_q and obs[1]>c_q
                clobs[3] = diagcloser( queen, obs, clobs[3] )
            elsif obs[0]>r_q and obs[1]>c_q
                clobs[5] = diagcloser( queen, obs, clobs[5] )
            elsif obs[0]>r_q and obs[1]<c_q
                clobs[7] = diagcloser( queen, obs, clobs[7] )
            end
        end

    }

#    puts "post"
#    p clobs

    pp = ( c_q-clobs[0][1] ) +
         ( c_q-clobs[1][1] ) +
         ( r_q-clobs[2][0] ) +
         ( r_q-clobs[3][0] ) +
         ( clobs[4][1]-c_q ) +
         ( clobs[5][1]-c_q ) +
         ( clobs[6][0]-r_q ) +
         ( clobs[7][0]-r_q ) + (-8)

    return pp

end

# fptr = File.open(ENV['OUTPUT_PATH'], 'w')
fptr = $stdout.dup

nk = gets.rstrip.split

n = nk[0].to_i

k = nk[1].to_i

r_qC_q = gets.rstrip.split

r_q = r_qC_q[0].to_i

c_q = r_qC_q[1].to_i

obstacles = Array.new(k)

k.times do |i|
    obstacles[i] = gets.rstrip.split(' ').map(&:to_i)
end

result = queensAttack n, k, r_q, c_q, obstacles

fptr.write result
fptr.write "\n"

fptr.close()


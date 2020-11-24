#!/bin/ruby

require 'json'
require 'stringio'

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c)

#    puts "len "+c.length.to_s
    
    p = 0
    x = 0
    while x<c.length-1 do
#        puts "gehen x=" + x.to_s + "/ c[x]=" + c[x].to_s + "] / p="+p.to_s
        if x+3>=c.length
            x=x+1
        else
            if c[x+2]==1
            else
                x=x+1
            end
        end
        p=p+1
        x=x+1
    end

    return p
end

if(ENV['OUTPUT_PATH'] )
    fptr = File.open(ENV['OUTPUT_PATH'], 'w')
else
    fptr = $stdout.dup
end

n = gets.to_i

c = gets.rstrip.split(' ').map(&:to_i)

result = jumpingOnClouds c

fptr.write result
fptr.write "\n"

fptr.close()


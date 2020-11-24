#!/bin/ruby

require 'json'
require 'stringio'

# Complete the repeatedString function below.
def repeatedString(s, n)

    p = n % s.length
    if s.length>n then 
        sc=0
        p=n
    else 
        sc = s.count( 'a' ) 
    end
    if p==0 then 
        sp=0 
    else 
        sp=s[0..p-1].count( 'a' ) 
    end

#    puts "p="+p.to_s+" sc="+sc.to_s+" sp="+sp.to_s+" n/len="+(n/s.length).to_s

    return ((n/s.length)*sc)+sp
end

if(ENV['OUTPUT_PATH'] )
    fptr = File.open(ENV['OUTPUT_PATH'], 'w')
else
    fptr = $stdout.dup
end

s = gets.to_s.rstrip

n = gets.to_i

result = repeatedString s, n

fptr.write result
fptr.write "\n"

fptr.close()


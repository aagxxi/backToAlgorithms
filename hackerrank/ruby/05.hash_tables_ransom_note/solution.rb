#!/bin/ruby

require 'json'
require 'stringio'

# Complete the checkMagazine function below.
def djb2 str
    hash = 5381
    str.each_byte do |b|
      hash = (((hash << 5) + hash) + b) % (2 ** 32)
    end
    hash
end

def checkMagazine(magazine, note)

  idx = Hash.new(nil)
  magazine.each do |word|
    if idx[word]==nil then
      idx[word]=1
    else
      idx[word]=idx[word]+1
    end
  end
  formed=true
  note.each do |word|
    if idx[word]==nil then
      formed=false
    else
      if idx[word]==0 then
        formed=false
      else
        idx[word]=idx[word]-1
      end
    end
  end

  if formed then
    puts "Yes"
  else
    puts "No"
  end

end


mn = gets.rstrip.split

m = mn[0].to_i

n = mn[1].to_i

magazine = gets.rstrip.split(' ').map(&:to_s)

note = gets.rstrip.split(' ').map(&:to_s)

checkMagazine magazine, note

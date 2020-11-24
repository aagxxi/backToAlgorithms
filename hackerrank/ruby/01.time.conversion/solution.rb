#!/bin/ruby

#
# Complete the timeConversion function below.
#
def timeConversion(s)
    #
    # Write your code here.
    #
    hr = s[0..1]
    hi = hr.to_i
    ap = s[8..9]
    mi = s[2..7].upcase

    if hi<12
        if ap=="PM"
            rr = (hi + 12).to_s.rjust(2, "0") + mi
        else
            rr = hr + mi
        end
    else
        if ap=="AM"
            rr = "00" + mi
        else
            rr = "12" + mi
        end
    end

    return rr
end

# fp = File.open(ENV['OUTPUT_PATH'], 'w')
fp = $stdout.dup

s = gets.to_s.rstrip

result = timeConversion s

fp.write result
fp.write "\n"

fp.close()


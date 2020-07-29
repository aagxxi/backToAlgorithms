#!/usr/bin/ruby

require 'open3'
require 'tempfile'

$known_interpreters = { ".JAVA" => "java.sh",
                        ".RB" => "ruby.sh",
                        ".JS" => "nodejs.sh",
                        ".C" => "c.sh",
#                        ".PY" => "/usr/bin/python3"                         
                        ".PY" => "python.sh" 
                    }

def solution_filename()
    Dir.foreach(".") do |fn|
        ext = File.extname( fn )
#        puts "extname=>" + ext
        if $known_interpreters[ ext.upcase ]
            fln = File.basename( fn, ext )
#            puts "basename=>" + fln.upcase
            if fln.upcase == "SOLUTION"
                return [ $known_interpreters[ ext.upcase ], fln, ext ]
            end
        end
    end
end

def compare_results( fn1, fn2 )

    r1 = fn1.readlines()
    r2 = fn2.readlines()

    l = 0
    while ( l < r1.length() )or( l < r2.length() )
        if l>=r1.length()
            c1=nil
        else
            c1=r1[l].gsub(/[\s\n]+/, "")
            if c1.empty?
                c1=nil
            end
        end
        if l>=r2.length()
            c2=nil
        else
            c2=r2[l].gsub(/[\s\n]+/, "")
            if c2.empty?
                c2=nil
            end
        end

        #puts "esta linea:" + c1
        #puts "otra linea:" + c2

        if c1 != c2
            return false
        end

        l=l+1
    end

    return true

end

def run_command( inp, sco )

    pwd = Dir.pwd
    input_file = File.join( pwd, "input", inp )
    output_file = File.join( pwd, "output", inp.gsub('input', 'output') )
    solution_script = File.join( pwd, sco[1] )
    my_wrapper = File.join( File.expand_path(File.dirname(__FILE__)), sco[0] )
#    my_wrapper = sco[0]
    tmp_file = Tempfile.new( 'testing' )

    if false
        puts "=input====>" + input_file
        puts "=output===>" + output_file
        puts "=solution=>" + solution_script
        puts "=wrapper==>" + my_wrapper
        puts "=testing==>" + tmp_file.path
    else
        puts "testing with input file \"" + inp + "\""        
    end

    # File.dirname(__FILE__)                     # relative path
    # File.expand_path(File.dirname(__FILE__))   # full path

    mystdin = File.open( input_file, "r" )
    myoutpt = File.open( output_file, "r" )
#    Open3.pipeline( my_wrapper + ' ' + solution_script, :in=>mystdin )
    res = Open3.pipeline( "/bin/bash " + my_wrapper + ' run "' + solution_script + '" ' + sco[1],
                          :in=>input_file, :out=>tmp_file )
#    spawn( my_wrapper + ' ' + solution_script, :in=>input_file )

    if res[0].exitstatus != 0
        puts "process returned error ( exitstatus=" + res[0].exitstatus.to_s + " )"
        return false
    end

    tmp_file.rewind 
    return compare_results( myoutpt, tmp_file )

end

def run_prepost( sco, pre )

    pwd = Dir.pwd
    solution_script = File.join( pwd, sco[1] )
    my_wrapper = File.join( File.expand_path(File.dirname(__FILE__)), sco[0] )
    tmp_file = Tempfile.new( 'testing' )

    if pre
        puts "running pre"
        pid = spawn( "/bin/bash " + my_wrapper + ' pre "' + solution_script + '" ' + sco[1] )
        Process.wait(pid)
        res = $?
    else
        puts "running post"
        pid = spawn( "/bin/bash " + my_wrapper + ' pos "' + solution_script + '" ' + sco[1] )
        Process.wait(pid) 
        res = $?
    end

    return res.exitstatus == 0
end

puts "hackerrank solutions"

filter = ARGV[0]
solution_code = solution_filename()
puts "run \"" + solution_code[ 1 ] + solution_code[ 2 ] + "\" with \"" + solution_code[ 0 ] + "\""
if filter then  puts "filtering input filenames by \""+filter+"\"" end
run_prepost( solution_code, true )

correct = true
Dir.foreach("./input/") do |filename|

    next if filename == '.' or filename == '..' or not correct
    if filter and not( filename.include? filter )
        puts "skipping \""+filename+"\""
        next
    end
    # Do work on the remaining files & directories

    # fln = File.basename( fn, ext )

    if run_command( filename, solution_code )
        puts( "correct" )
    else
        puts( "incorrect" )
        correct = false
    end

end

run_prepost( solution_code, false )

if correct
    puts( "CORRECT" )
else
    puts( "INCORRECT" )
end

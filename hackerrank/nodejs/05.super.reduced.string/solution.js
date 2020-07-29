'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the superReducedString function below.
function superReducedString(s) {

    // caso limite: x-1, ver

    var x;
    var r;

    x=0;
    r=s;
    while( x<=(r.length-1) )
    {
//        process.stdout.write( "x=" + x + " r=" + r + "\n" );
        if( r[x]==r[x+1] )
        {
            var p;
//            p = r;
            r = r.substring( 0,x ) + r.substring( x+2,r.length );
//            process.stdout.write( "p=" + p + " r=" + r + "\n" );
            if( x>0 ) { x--; }
            x--;
        }
        x++;
    }

    if( ! r.length )
    {
        r = "Empty String"
    }

    return r;
}

function main() {
    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }    

    const s = readLine();

    const result = superReducedString(s);

    ws.write(result + '\n');

    ws.end();
}


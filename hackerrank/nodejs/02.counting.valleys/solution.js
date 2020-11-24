'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countingValleys function below.
function countingValleys(n, s) {

    var i;
    var e = 0;
    var c = 0;
    for (i = 0; i < s.length; i++ ) {

        if ( s[i] == "U"  ) 
        { 
            e++; 
            if ( e==0 ) { c++; }
        }
        else if ( s[i] == "D" ) 
        { 
            e--; 
        }

//        process.stdout.write( "i=" + i + " s[]=" + s[i] + " elevation=" + e + "\n" );

    }

    return c;
}

function main() {

    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }

    const n = parseInt(readLine(), 10);

    const s = readLine();

    let result = countingValleys(n, s);

    ws.write(result + "\n");

    ws.end();
}

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

// Complete the camelcase function below.
function camelcase(s) {

    var c = 1;
    var x;
    for( x=0; x<s.length; x++ )
    {
        if( s.charCodeAt(x)<97 )
        {
            if( x!=0 ){ c++; }
        }

    }
    return c;
}

function main() {
    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }    

    const s = readLine();

    let result = camelcase(s);

    ws.write(result + "\n");

    ws.end();
}


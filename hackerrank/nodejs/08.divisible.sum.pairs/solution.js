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

// Complete the divisibleSumPairs function below.
function divisibleSumPairs(n, k, ar) {
    var i;
    var j;
    var q = 0;
    for ( i = 0; i < n-1; i++ ) {
        for ( j = i+1; j < n; j++ )
        {
            var s = ( ar[i]+ar[j] )% k;
            if ( ! s ) q++;
//            process.stdout.write( "i=" + i + " j=" + j + " s=" + s + " q=" + q + "\n" );
        }
    } 
    return q;
}

function main() {
    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }    

    const nk = readLine().split(' ');

    const n = parseInt(nk[0], 10);

    const k = parseInt(nk[1], 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = divisibleSumPairs(n, k, ar);

    ws.write(result + "\n");

    ws.end();
}

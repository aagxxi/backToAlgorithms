
'use strict';

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

// Complete the countApplesAndOranges function below.
function countApplesAndOranges(s, t, a, b, apples, oranges) {

    var i;
    var app = 0;
    var ora = 0;
    for (i = 0; i < apples.length; i++ ) {
        let p = apples[i]+a;
        if ( ( p>=s )&( p<=t ) ) { app++; }
//        process.stdout.write( "i=" + i + " rel a[]=" + apples[i] + " abs a[]=" + (apples[i]+a) + " app=" + app + "\n" );
    }
    for (i = 0; i < oranges.length; i++ ) {
        let p = oranges[i]+b;
        if ( ( p>=s )&( p<=t ) ) { ora++; }
//        process.stdout.write( "i=" + i + " rel o[]=" + oranges[i] + " abs o[]=" + (oranges[i]+b) + " ora=" + ora + "\n" );
    }

    process.stdout.write( app+"\n" );
    process.stdout.write( ora+"\n" );
}

function main() {
    const st = readLine().split(' ');

    const s = parseInt(st[0], 10);

    const t = parseInt(st[1], 10);

    const ab = readLine().split(' ');

    const a = parseInt(ab[0], 10);

    const b = parseInt(ab[1], 10);

    const mn = readLine().split(' ');

    const m = parseInt(mn[0], 10);

    const n = parseInt(mn[1], 10);

    const apples = readLine().split(' ').map(applesTemp => parseInt(applesTemp, 10));

    const oranges = readLine().split(' ').map(orangesTemp => parseInt(orangesTemp, 10));

    countApplesAndOranges(s, t, a, b, apples, oranges);
}


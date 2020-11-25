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

// Complete the minimumNumber function below.
function minimumNumber(n, password) {
    // Return the minimum number of characters to make the password strong

    const numbers = "0123456789";
    const lower_case = "abcdefghijklmnopqrstuvwxyz";
    const upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const special_characters = "!@#$%^&*()-+";

    var i;
    var t = [ 0, 0, 0, 0, 0 ];
    for ( i=0; i<n; i++ )
    {
        if ( numbers.includes( password[i] ) ) t[0]++;
        else if ( lower_case.includes( password[i] ) ) t[1]++;
        else if ( upper_case.includes( password[i] ) ) t[2]++;
        else if ( special_characters.includes( password[i] ) ) t[3]++;
        else t[4]++;
    }
    var a = 0;
    for ( i=0; i<4; i++ )
    {
        if ( t[i]==0 ) 
        {
            a++;
            t[i]++;
        }
    }
    var s = t[0]+t[1]+t[2]+t[3]+t[4];
    if( s<6 ) { a = a + 6-s; }

    return a;
}

function main() {
    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }    

    const n = parseInt(readLine(), 10);

    const password = readLine();

    let answer = minimumNumber(n, password);

    ws.write(answer + "\n");

    ws.end();
}


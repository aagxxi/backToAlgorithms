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

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function getTotalX(a, b) {
    // Write your code here
 
     if( a.length == 0 | b.length == 0 )
     {
         return 0;
     }
 
     a.sort()
     b.sort()
 
     var x;
     var restop = b[ 0 ];
     var resbot = a[ a.length-1 ];
     var valid = new Array( b[ b.length-1 ]+1 );
 
     valid.fill(0);
 
     function mark( n ){
         var i = 1;
         while( (i * i)<n ) {
             if( ( n % i ) == 0 ) { 
                 valid[ i ]++;
                 valid[ n / i ]++;
             }
             i++;
         }
         if( ( i * i ) == n )
         {
             valid[ i ]++;
         }
     }
 
     function verify( n ){
         var i = a.length - 1;
         while( i>=0 & valid[n]==b.length )
         {
             if( ( n % a[i] ) != 0 )
             {
                 valid[n] = 0;
             }
             i--;
         }
     }
 
     for( x=b.length - 1; x >= 0; x-- )
     {
         mark( b[x] ); 
     }
 
     var r = 0;
     for ( x=resbot; x<=restop; x++ )
     {
         verify( x );
         if( valid[x] == b.length )
         {
             r++;
         }
     }
 
     return r;
 }
 

function main() {
    let ws = process.stdout;
    if ( process.env.OUTPUT_PATH ) {
        ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    }    

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const brr = readLine().replace(/\s+$/g, '').split(' ').map(brrTemp => parseInt(brrTemp, 10));

    const total = getTotalX(arr, brr);

    ws.write(total + '\n');

    ws.end();
}


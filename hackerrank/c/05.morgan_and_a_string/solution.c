#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();

// Complete the morganAndString function below.

// Please either make the string static or allocate on the heap. For example,
// static char str[] = "hello world";
// return str;
//
// OR
//
// char* str = "hello world";
// return str;
//
char* morganAndString(char* a, char* b) {

    char* rstr;
    int la = strlen( a );
    int lb = strlen( b );
    int ltot = la + lb + 2;
    int pa = 0;
    int pb = 0;
    int pt = 0;

    rstr = malloc( ltot );

// cc solution.c ; cat input/input96.txt | ./a.out ; echo --- ; cat output/output96.txt

    while( ( pa < la )&&( pb < lb ) )
    {

        if ( a[pa]<b[pb] ) {
            rstr[pt] = a[pa];
            pt++;
            pa++;
        }else if ( a[pa]>b[pb] ) {
            rstr[pt] = b[pb];
            pt++;
            pb++;
        }else{
            char eq = a[pa];
            int ka = pa;
            int kb = pb;
            int ix = pb;
            while( ( ka<la )&&( kb<lb )&&( a[ka]==b[kb] ) )
            {
//                printf( "pre ix=%d a[ka]:b[kb]=%c:%c eq=%d\n", ix, a[ka], b[kb], eq );
                ka++;
                if ( ( ix == kb )&&( eq>=a[ka] )&&( a[ka-1]>=a[ka] ) ) { ix++; }
                kb++;
            }
            
            #define max(x,y) (((x) > (y)) ? (x) : (y))
            ix = max( ix - pb, 1 );
//            if ( ix>=0 ) { printf( "ix=%d \n", ix, pb ); }
            if( ( ka<la )&&( kb<lb ) )
            {
                if( a[ka]<b[kb] ) 
                { 
                    ka = pa + ix;
                    kb = pb; 
                }
                else 
                { 
                    ka = pa; 
                    kb = pb + ix;
                }
            }else{
                if( ka<la )
                { 
                    ka = pa + ix;
                    kb = pb; 
                }
                else 
                { 
                    ka = pa; 
                    kb = pb + ix;
                }
            }
//            printf( "pre while pa=%d pb=%d ka=%d kb=%d\n", pa, pb, ka, kb );
            while( pa < ka ){
                            rstr[pt] = a[pa];
                            pt++;
                            pa++;
            }
            while( pb < kb ){
                            rstr[pt] = b[pb];
                            pt++;
                            pb++;
                        }



/**            
            if( ( ka<la )&&( kb<lb ) )
            {
                if( a[ka]<b[kb] )
                { 
                    rstr[pt] = a[pa];
                    pt++;
                    pa++;
                }else{
                    rstr[pt] = b[pb];
                    pt++;
                    pb++;
                }
            }else{
                if( ka<la )
                { 
                    rstr[pt] = a[pa];
                    pt++;
                    pa++;
                }else{
                    rstr[pt] = b[pb];
                    pt++;
                    pb++;
                }
            }
*/

        }
    }

/**
                if( a[ka]!=b[kb] ) break;
                else if ( a[ka] > eq ) {
                    while( pa < ka )
                    {
                        rstr[pt] = a[pa];
                        pt++;
                        pa++;
                    }
                    while( pb < kb ) 
                    {
                        rstr[pt] = b[pb];
                        pt++;
                        pb++;
                    }
                    eq = a[pa];
                }
                if( ka==la ) {
                    rstr[pt] = b[pb];
                    pt++;
                    pb++;
                }else if( kb==lb ) {
                    rstr[pt] = a[pa];
                    pt++;
                    pa++;
                }else{
                    if ( a[ka] < b[kb] ) {
                        rstr[pt] = a[pa];
                        pt++;
                        pa++;
                    }else{
                        rstr[pt] = b[pb];
                        pt++;
                        pb++;
                    }
                }
                ka++;
                kb++;
*/                

    while( pa < la ){
                    rstr[pt] = a[pa];
                    pt++;
                    pa++;
    }
    while( pb < lb ){
                    rstr[pt] = b[pb];
                    pt++;
                    pb++;
                }
    
    rstr[pt] = 0;

    return rstr;
}

int main()
{
    FILE* fptr;
    if ( getenv("OUTPUT_PATH") == NULL  )
    {
        fptr = stdout;
    }else{
        fptr = fopen(getenv("OUTPUT_PATH"), "w");
    }    

    char* t_endptr;
    char* t_str = readline();
    int t = strtol(t_str, &t_endptr, 10);

    if (t_endptr == t_str || *t_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int t_itr = 0; t_itr < t; t_itr++) {
        char* a = readline();

        char* b = readline();

        char* result = morganAndString(a, b);

        fprintf(fptr, "%s\n", result);
    }

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

/*
 * Complete the legoBlocks function below.
 */

long long one_cache[1001] = {[0 ... 1000]=-1};

int legoBlocks(int n, int m) {
    /*
     * Write your code here.
     */
    long long modpow_cache[1001] = {[0 ... 1000]=-1};
    long long solid_cache[1001] = {[0 ... 1000]=-1};

    long long one( int i ) {
        one_cache[ 0 ] = 1;
        one_cache[ 1 ] = 1;
        one_cache[ 2 ] = 2;
        one_cache[ 3 ] = 4;
        for ( int x=4; x<=i; x++ ) { //  in range( 4, i+1 ):
          one_cache[ x ] = ( one_cache[ x-1 ]+one_cache[ x-2 ]+one_cache[ x-3 ]+one_cache[ x-4 ] ) % 1000000007;
        }
        return one_cache[ i ];
    } 

    long long modpow( int i, int j )
    {
        for( int x=1; x<=i; x++ ) {
            long long result = 1;
            long long exp = (long long)j;
            long long base = one_cache[x];
            for (;;)
            {
                if (exp & 1) result = ( result * base ) % 1000000007;
                exp >>= 1;
                if (!exp) break;
                base = ( base * base ) % 1000000007;
            }
            modpow_cache[x] = result;
        }
        return modpow_cache[i];
    }

    long long solid( int n, int i )
    {
//        printf( "solid %dx%d", n ,i );
        if ( solid_cache[i]>=0 ) { return solid_cache[i]; }
        if ( n==1 )
        {
            if ( i>4 ) { solid_cache[i]=0; return 0; }else{ solid_cache[i]=1; return 1; }
        }
        long long broke = 0;
        for( int x=1; x<i; x++ ) {
            broke = ( broke + solid( n,x ) * modpow_cache[i-x] ) % 1000000007;
        }
        solid_cache[i] = ( modpow_cache[i] - broke + 1000000007 )% 1000000007;
        return solid_cache[i];
    }

    if ( one_cache[ m ] < 0 ) { one( m ); }
    if ( modpow_cache[ m ] < 0 ) { modpow( m,n ); }

    int r = (int)solid( n, m ) % 1000000007;
    return r;
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
        char** nm = split_string(readline());

        char* n_endptr;
        char* n_str = nm[0];
        int n = strtol(n_str, &n_endptr, 10);

        if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

        char* m_endptr;
        char* m_str = nm[1];
        int m = strtol(m_str, &m_endptr, 10);

        if (m_endptr == m_str || *m_endptr != '\0') { exit(EXIT_FAILURE); }

        int result = legoBlocks(n, m);

        fprintf(fptr, "%d\n", result);
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

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

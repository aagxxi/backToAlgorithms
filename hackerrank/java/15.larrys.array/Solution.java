import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static int[] A;

    static void rotate( int i ) {

        int t;

        t = A[i];
        A[i] = A[i+1];
        A[i+1] = A[i+2];
        A[i+2] = t;
    }

    static Boolean bringme( int i, int j ) {

//        System.out.println( "bringme "+(i)+" to position "+(j+1)+" / A="+Arrays.toString(A) );

        if( j<A.length-3 )
        {
            if( A[j+1]==i ) 
            { 
                rotate( j );
                return true;
            }
            if( bringme( i, j+1 ) )
            {
                rotate( j );
                return true;
            }else{
                return false;
            }
        }else if( j==A.length-3 ) {
            if( A[j+1]==i ) { rotate( j ); }
            else { rotate( j ); rotate( j ); }
            return true;
        }else{
            return ( j==A.length-1 )&&( A[j]==1 );
        }

    }

    // Complete the larrysArray function below.
    static String larrysArray(int[] ingressingA) {

        A = ingressingA;

        int x;
        Boolean possible = true;

//        System.out.println( "starting" );
        for ( x=0; ( x<A.length )&&( possible ); x++ ) 
        {
//            System.out.println( "is "+(x+1)+" in position? / A="+Arrays.toString(A) );
            if ( (x+1)!=A[x] )
            {
                possible = bringme( x+1, x );
            }
        }

        return possible ? "YES" : "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter;
        if ( System.getenv("OUTPUT_PATH") != null )
        {
            bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        }else{
            bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] A = new int[n];

            String[] AItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int AItem = Integer.parseInt(AItems[i]);
                A[i] = AItem;
            }

            String result = larrysArray(A);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}


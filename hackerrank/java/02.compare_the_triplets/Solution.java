import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the solve function below.
     */
    static int[] solve(int a0, int a1, int a2, int b0, int b1, int b2) {
        /*
         * Write your code here.
         */

	int[] rr = new int[ 2 ];
	rr[ 0 ] = 0;
	rr[ 1 ] = 0;

	if ( a0 > b0 )
	{
		rr[ 0 ]++;
	}
	else if( b0 > a0 )
	{
		rr[ 1 ]++;
	}

	if ( a1 > b1 )
	{
		rr[ 0 ]++;
	}else if( b1 > a1 )
	{
		rr[ 1 ]++;
	}

	if ( a2 > b2 )
	{
		rr[ 0 ]++;
	}else if( b2 > a2 )
	{
		rr[ 1 ]++;
	}

	return rr;

    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        BufferedWriter bw;
        if ( System.getenv( "OUTPUT_PATH" ) == null )
        {
//                System.out.println( "is null" );
                bw = new BufferedWriter( new OutputStreamWriter(System.out) );
        }else{
//                System.out.println( "is not null" );
                bw = new BufferedWriter(new FileWriter(System.getenv( "OUTPUT_PATH" )));
        }

        String[] a0A1A2 = scan.nextLine().split(" ");

        int a0 = Integer.parseInt(a0A1A2[0].trim());

        int a1 = Integer.parseInt(a0A1A2[1].trim());

        int a2 = Integer.parseInt(a0A1A2[2].trim());

        String[] b0B1B2 = scan.nextLine().split(" ");

        int b0 = Integer.parseInt(b0B1B2[0].trim());

        int b1 = Integer.parseInt(b0B1B2[1].trim());

        int b2 = Integer.parseInt(b0B1B2[2].trim());

        int[] result = solve(a0, a1, a2, b0, b1, b2);

        for (int resultItr = 0; resultItr < result.length; resultItr++) {
            bw.write(String.valueOf(result[resultItr]));

            if (resultItr != result.length - 1) {
                bw.write(" ");
            }
        }

        bw.newLine();

        bw.close();
    }
}

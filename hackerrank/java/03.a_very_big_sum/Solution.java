import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the aVeryBigSum function below.
     */
    static long aVeryBigSum(int n, long[] ar) {
        /*
         * Write your code here.
         */

	long r = 0;

	for ( int x=0; x<n; x++ )
	{
		r = r + ar[ x ];
	}

	return r;

    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

        BufferedWriter bw;
        if ( System.getenv( "OUTPUT_PATH" ) == null )
        {
                bw = new BufferedWriter( new OutputStreamWriter(System.out) );
        }else{
                bw = new BufferedWriter(new FileWriter(System.getenv( "OUTPUT_PATH" )));
        }

        int n = Integer.parseInt(scan.nextLine().trim());

        long[] ar = new long[n];

        String[] arItems = scan.nextLine().split(" ");

        for (int arItr = 0; arItr < n; arItr++) {
            long arItem = Long.parseLong(arItems[arItr].trim());
            ar[arItr] = arItem;
        }

        long result = aVeryBigSum(n, ar);

        bw.write(String.valueOf(result));
        bw.newLine();

        bw.close();
    }
}
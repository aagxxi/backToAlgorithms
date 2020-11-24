import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

// https://www.hackerrank.com/challenges/simple-array-sum/problem

public class Solution {

    /*
     * Complete the simpleArraySum function below.
     */
    static int simpleArraySum(int[] ar) {
        /*
         * Write your code here.
         */

	int r = 0;

	for ( int x=0; x<ar.length; x++ )
	{
		r = r + ar[ x ];
	}

	return r;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {

	BufferedWriter bufferedWriter;
	if ( System.getenv( "OUTPUT_PATH" ) == null )
	{
//		System.out.println( "is null" );
        bufferedWriter = new BufferedWriter( new OutputStreamWriter(System.out) );
	}else{
//		System.out.println( "is not null" );
        bufferedWriter = new BufferedWriter(new FileWriter(System.getenv( "OUTPUT_PATH" )));
	}

        int arCount = Integer.parseInt(scanner.nextLine().trim());

        int[] ar = new int[arCount];

        String[] arItems = scanner.nextLine().split(" ");

        for (int arItr = 0; arItr < arCount; arItr++) {
            int arItem = Integer.parseInt(arItems[arItr].trim());
            ar[arItr] = arItem;
        }

        int result = simpleArraySum(ar);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}

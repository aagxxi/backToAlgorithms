import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the hurdleRace function below.
    static int hurdleRace(int k, int[] height) {

        int hh=height[0];
        for ( int x=0; height.length>x; x++ )
        {
            if ( height[x]>hh ) { hh=height[x]; };
        }
        if ( hh>k )
        {
            return hh-k;
        }else{
            return 0;
        }

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        
		BufferedWriter bufferedWriter;
		if ( System.getenv( "OUTPUT_PATH" ) == null )
		{
			bufferedWriter = new BufferedWriter( new OutputStreamWriter(System.out) );
		}else{
			bufferedWriter = new BufferedWriter(new FileWriter(System.getenv( "OUTPUT_PATH" )));
		}        

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] height = new int[n];

        for (int i = 0; i < n; i++) {
            int heightItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            height[i] = heightItem;
        }

        int result = hurdleRace(k, height);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class AddTwoNumbers {


    static int addMeFirst(int a, int b) {
        return a+b;
   }

   
 public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a;
        a = in.nextInt();
        int b;
        b = in.nextInt();
        int sum;
	if((a>=1 &&b>=1)&&(a<=1000&&b<=1000)){
       		sum = addMeFirst(a, b);
        	System.out.println(sum);
	}
   }
}


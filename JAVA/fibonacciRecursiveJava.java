    import java.util.Arrays;
    import java.util.Scanner;
     
    public class fibonacciRecursiveJava {
     
      public static void main(String args[]) {
        fibonacciSeries(11);
        fibonacciSeries(12);
      }
       
      public static void fibonacciSeries(int number) {
        System.out.printf("\nFibonacci series in Java of number %s using recursion %n", number);
        for (int i = 1; i <= number; i++) {
        System.out.printf("%s ", getFibonacci(i));
        }
      }
      
      public static int getFibonacci(int n) {
        if (n == 1) {
          return 1;
        }
        if (n == 2) {
          return 1;
        }
        return getFibonacci(n - 1) + getFibonacci(n - 2);
      }
     
    }

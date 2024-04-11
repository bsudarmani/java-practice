import java.util.*;
import java.io.*;
public class LCMRecursion 
{
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the 1st num");
        int a=sc.nextInt();
        System.out.println("enter the 2nd num");
        int b=sc.nextInt();
        int gcd = 1;

        for (int i = 1; i <= a && i <= b; ++i)
         {

            if (a % i == 0 && b % i == 0)
                gcd = i;
        }
       
        int lcm = (a * b) / gcd;
        System.out.printf("The LCM of %d and %d is %d.", a, b, lcm);
    }
}

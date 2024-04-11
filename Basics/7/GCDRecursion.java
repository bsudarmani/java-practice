import java.util.*;
import java.io.*;
public class GCDRecursion
{
 public static void main(String args[])
 {
    Scanner sc=new Scanner(System.in);
     System.out.println("enter first num");
     int num1=sc.nextInt();
     System.out.println("enter seond num");
     int num2=sc.nextInt();
     int gcd=calculate(num1,num2);
     System.out.println("num1 "+ num1 + "num2 "+ num2 + " gcd "+ gcd);
 }    
 public static int calculate(int n1,int n2)
 {
    if(n2==0)
    {
        return n1;
    }
    return calculate(n2, n1 % n2);
 }
}

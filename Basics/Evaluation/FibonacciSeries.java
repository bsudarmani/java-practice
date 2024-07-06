import java.util.*;
import java.io.*;
class  FibonacciSeries
{
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("Enter the number");
 int n=sc.nextInt();
 int s1=0,s2=1,s3=0;
 System.out.print(s1 + " " + s2);
 while(s1<=n)
 {
 s3=s1+s2;
  System.out.print(" "+ s3);
  s1=s2;
  s2=s3;
 }
}
} 
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
 System.out.println(s1 + " " + s2);
 for(int i=0;i<n;i++)
 {
 s3=s1+s2;
  System.out.println(s3);
  s1=s2;
  s2=s3;
 }
}
} 
import java.util.*;
import java.io.*;
class CalculateAvg
{
 public static void main(String args[])
 { Scanner sc=new Scanner(System.in);
 System.out.println("enter the number of element");
 int n=sc.nextInt(); 
 int sum=0;
 double avg=0;
 int number[]=new int[n];
 System.out.println("enter the number");
 for(int i=0;i<n;i++)
 {
  number[i]=sc.nextInt();
 sum=sum+number[i];
 }
 System.out.println("sum of numbers:"+sum);
  avg=(double)sum/n;
 System.out.println("Avg of numbers:"+avg);
 }
}
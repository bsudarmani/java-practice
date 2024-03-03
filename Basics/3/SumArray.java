import java.util.*;
import java.io.*;
class SumArray
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array:");
     int num=sc.nextInt();
     int number[]=new int[num];
     int sum=0;
     System.out.println("Enter the number in one by one");
     for(int i=0;i<num;i++)
     {  
     number[i]=sc.nextInt();
     }
     for(int i=0;i<num;i++)
     {
     sum+=number[i];
     }
     System.out.println("sum of Integers:"+sum);
    }
}
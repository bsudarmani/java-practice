import java.util.*;
import java.io.*;
class AverageDouble
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array:");
     int num=sc.nextInt();
     double number[]=new double[num];
     double sum=0;
     System.out.println("Enter the number in one by one");
     for(int i=0;i<num;i++)
     {  
     number[i]=sc.nextDouble();
     } 
     for(int i=0;i<num;i++)
     {
    sum+=number[i];
     }
     double avg=sum/number.length;
     System.out.println("Average of all element in array of Double:"+avg);
    }
}
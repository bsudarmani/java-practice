import java.util.*;
import java.io.*;
class SmallestLargest
{
    public static void main(String args[])
    {
      Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array:");
     int num=sc.nextInt();
     int number[]=new int[num];
     System.out.println("Enter the number in one by one");
     for(int i=0;i<num;i++)
     {  
     number[i]=sc.nextInt();
     } 
     int large=number[0];
     int small=number[0];
     for(int i=0;i<num;i++)
     {
        if(number[i]>large)
        {
           large=number[i];
        }
     }
     for(int i=0;i<num;i++)
     {
        if(number[i]<small)
        {
            small=number[i];
        }
     }
     System.out.println("Smallest element in array : "+ small);
     System.out.println("Largest element in array : "+large);
    }
}
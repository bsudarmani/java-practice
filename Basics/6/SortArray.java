import java.util.*;
import java.io.*;
class SortArray
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
     System.out.println("ascending order : ");
     for(int i=0;i<number.length;i++)
     {
        for(int j=i+1;j<number.length;j++)
        {
            if(number[i]>number[j])
            {
                int temp=number[i];
                number[i]=number[j];
                number[j]=temp;
            }
        }
           System.out.println(number[i]);
     }
     System.out.println("descending order : ");
     for(int i=0;i<number.length;i++)
     {
        for(int j=i+1;j<number.length;j++)
        {
            if(number[i]<number[j])
            {
                int temp=number[i];
                number[i]=number[j];
                number[j]=temp;
            }
        }
        System.out.println(number[i]);
     }
    }
}
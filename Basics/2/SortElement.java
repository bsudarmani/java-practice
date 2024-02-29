import java.util.*;
import java.io.*;
class SortElement
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array");
     int num=sc.nextInt();
      int number[]=new int[num];
     int arr1[]=new int[num];
     int arr2[]=new int[num];
     int odd=0,even=0;
      System.out.println("enter the element in one by one");
     for(int i=0;i<num;i++)
     {
        number[i]=sc.nextInt();
     }
     for(int i=0;i<num;i++)
     {
        if(number[i]%2!=0)
         {
            arr1[even++]=number[i];
         }
         else
         {
            arr2[odd++]=number[i];
         }
     }
     for(int i=0;i<num;i++)
     {
     System.out.println(arr1[i]);
     System.out.println(arr2[i]);
     }
    }
}
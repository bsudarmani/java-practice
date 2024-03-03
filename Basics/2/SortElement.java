import java.util.*;
import java.io.*;
class SortElement
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array");
     int num=sc.nextInt();
     int arr1[]=new int[100];
     int arr2[]=new int[100];
     int odd=0,even=0;
      System.out.println("enter the element in one by one");
     for(int i=0;i<num;i++)
     {
        if(i%2!=0)
         {
            arr1[even]=sc.nextInt();
            even++;
         }
         else
         {
            arr2[odd]=sc.nextInt();
            odd++;
         }
     }
     for(int i=0;i<odd-1;i++)
     {
       for(int j=i+1;j<odd;j++)
       {
         if(arr2[i]<arr2[j])
         {
            int temp=arr2[i];
            arr2[i]=arr2[j];
            arr2[j]=temp;
         }
       }
     }
     for(int i=0;i<even-1;i++)
     {
      for(int j=i+1;j<even;j++)
      {
       if(arr1[i]>arr1[j])
       {
          int temp=arr1[i];
          arr1[i]=arr1[j];
          arr1[j]=temp;
       }
      }
     }
     int len=odd>even?odd:even;
     for(int i=0;i<len;i++)
     {
      if(i<odd)
      {
         System.out.print(" "+arr2[i]);
      }
      if(i<even)
      {
         System.out.print(" "+arr1[i]);
      }
     }
    }
}
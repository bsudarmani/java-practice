import java.util.*;
import java.io.*;
class RotateArray
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("enter the number in array:");
     int num=sc.nextInt();
     int arr[]=new int[num];
     System.out.println("enter the number in array one by one");
     for(int i=0;i<arr.length;i++)
     {
        arr[i]=sc.nextInt();
     }
     System.out.println("enter the number to rotate in array:");
     int digit=sc.nextInt();
     findrotate(arr,num,digit);
    }
    public static void findrotate(int arr[],int num,int digit)
    {
        System.out.println("original array:"+ Arrays.toString(arr));
        int temp[]=new int[num];
        int k=0;
        for(int i=digit;i<arr.length;i++)
        {
            temp[k]=arr[i];
            k++;
        }
        for(int i=0;i<digit;i++)
        {
            temp[k]=arr[i];
            k++;
        }
        for(int i=0;i<arr.length;i++)
        {
            arr[i]=temp[i];
        }
      System.out.println("rotate array:"+Arrays.toString(arr));
    }
}
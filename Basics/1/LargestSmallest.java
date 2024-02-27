import java.util.*;
import java.io.*;
class LargestSmallest
{
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("Enter the element of array");
 int num=sc.nextInt();
 int arr[]=new int[num];
 System.out.println("Number of element");
 for(int i=0;i<num;i++)
 {
 arr[i]=sc.nextInt();
 }
 int large=arr[0];
 int small=arr[0];
 System.out.println(large);
 System.out.println(small);
 for(int i=0;i<num;i++)
 {
  if(large<arr[i])
   large=arr[i];
  else if(small>arr[i])
   small=arr[i];
 }
 System.out.println("largest number is : "+ large);
 System.out.println("smallest number is : "+ small);
}
}
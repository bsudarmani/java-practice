import java.util.*;
import java.io.*;
class ThirdLargest
{
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("Enter the no of element in array");
 int num=sc.nextInt();
 int numbers[]=new int[num];
 System.out.println("enter the numbers in array");
 for(int i=0;i<num;i++)
 {
 numbers[i]=sc.nextInt();
 }
 int result=thirdlargest(numbers);
 System.out.println(result);
 }

 public static int thirdlargest(int number[])
 {
  if(number.length<3) 
  { 
   return -1;
  }
  else if(number.length>3)
  {
   for(int i=0;i<number.length;i++)
   {
    for(int j=i+1;j<number.length;j++)
    {
     if(number[i]==number[j])
      return 1;
    }
   }
  }
  return 0;
 }
}
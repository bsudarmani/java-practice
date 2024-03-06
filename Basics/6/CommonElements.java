import java.util.*;
import java.io.*;
class CommonElements
{
    public static void main(String args[])
    {
      Scanner sc=new Scanner(System.in);
       System.out.println("enter the no in 1st array");
       int num1=sc.nextInt();
       System.out.println("enter the no in 2nd array");
       int num2=sc.nextInt();
       int number1[]=new int[num1];
       int number2[]=new int[num2];
      System.out.println("Enter the number 1st array  in one by one");
      for(int i=0;i<number1.length;i++)
      {  
      number1[i]=sc.nextInt();
      } 

    System.out.println("Enter the number 2st array  in one by one");
      for(int i=0;i<number2.length;i++)
      {  
      number2[i]=sc.nextInt();
      } 
      for(int i=0;i<number1.length;i++)
      {
        for(int j=0;j<number2.length;j++)
        {
            if(number1[i]==(number2[j]))
             {
                System.out.println("common element : "+ (number1[i]));
             }
        }
      }
    }
}
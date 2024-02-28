import java.util.*;
import java.io.*;
class FindIndex
{
    public static void main(String args[])
    {
         Scanner sc=new Scanner(System.in);
         System.out.println("Enter the element in array");
         int num=sc.nextInt();
         int number[]=new int[num];
         System.out.println("Enter the element one by one in array");
         for(int i=0;i<number.length;i++)
         {
            number[i]=sc.nextInt();
         }
         System.out.println("Enter the number");
         int index=sc.nextInt();
          for(int i=0;i<number.length;i++)
          {
            if(index==number[i])
             {
            System.out.println(i);
            break;
             }
             else
             {
                System.out.println("-1");
                break;
             }
          }
    }
}
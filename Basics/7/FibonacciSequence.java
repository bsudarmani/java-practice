import java.util.*;
import java.io.*;
class  FibonacciSequence
{
    public static void main(String args[])
    {
         Scanner sc=new Scanner(System.in);
         System.out.println("enter the limit ");
         int limit=sc.nextInt();
         int n1=0,n2=1,n3=0;
         for(int i=1;i<=limit;i++)
         {
            System.out.println(""+n1);
            n3=n1+n2;
            n1=n2;
            n2=n3;
         }
    }
}
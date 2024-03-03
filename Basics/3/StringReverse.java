import java.util.*;
import java.io.*;
class StringReverse
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the no of string in array:");
     int num=sc.nextInt();
     String names[]=new String[num];
     System.out.println("Enter the String in one by one");
     for(int i=0;i<num;i++)
     {  
     names[i]=sc.next();
     }
     System.out.println("Reverse Order:");
     for(int i=names.length-1;i>=0;i--)
     {
        System.out.println(names[i]);
     }
    }
}
import java.util.*;
import java.io.*;
class ReverseString
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the String");
     String str=sc.next();
     String strrev="";
     for(int i=str.length()-1;i>=0;i--)
     {
        strrev+=str.charAt(i);
        
     }
      System.out.println(strrev);
    
    }
}
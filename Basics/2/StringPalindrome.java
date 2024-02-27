import java.util.*;
import java.io.*;
class StringPalindrome
{
 public static void main(String args[])
 {
  boolean t1=true;
  Scanner sc=new  Scanner(System.in);
  System.out.println("Enter the string");
  String str=sc.next();
  str=str.toLowerCase();
  for(int i=0;i<str.length()/2;i++)
  {
   if(str.charAt(i)!=str.charAt(str.length()-i-1))
   t1=false;
   break;
  }
 if(t1)
  System.out.println("true");
 else
  System.out.println("false");
 }
}
import java.util.*;
import java.io.*;
class StringPalindrome
{
public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("enter the string");
 String str=sc.next();
 boolean t1=validate(str);
 if(t1)
  System.out.println("palindrome");
 else
  System.out.println("Not palindrome");
 }
 public static  boolean validate(String str)
 {
 str=str.toLowerCase();
 str = str.replaceAll("[^a-zA-Z0-9]", "");
 int i=0;
 int j=str.length()-1;
 while(j>i)
 {
  if(str.charAt(i)!=str.charAt(j))
  {
   return false;
  }
  i++;
 j--;
  }
 return true;
 }
}
 
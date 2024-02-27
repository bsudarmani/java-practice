import java.util.*;
import java.io.*;
class ContainsString
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("enter your string:");
  String str=sc.next(); 
  boolean bool=str.contains("java");
  if(bool)
   {
   System.out.println("The String contains java");
   }
 else
  {
   System.out.println("The String not contains java");
  }  
 }
}
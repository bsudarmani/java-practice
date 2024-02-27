import java.util.*;
import java.io.*;
class VowelsString
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter the string");
  String str=sc.next();
  str=str.toLowerCase();
  boolean t1=vowel(str);
  System.out.println("Vowel:"+t1);
 }
public static  boolean vowel(String str)
 {
  for(int i=0;i<str.length();i++)
  { 
    char ch=str.charAt(i);
    if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
    return true;
  }
 return false;
 }
}
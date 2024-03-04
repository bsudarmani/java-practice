import java.util.*;
import java.io.*;
class  Anagrams
{
    public static void main(String args[])
    {
      Scanner sc=new Scanner(System.in);
      System.out.println("enter the first string :");
      String str1=sc.next();
      System.out.println("enter the second string:");
      String str2=sc.next();
      String s1=str1.replaceAll("\\s","");
      String s2=str2.replaceAll("\\s","");
      boolean t1=true;
      if(s1.length()!=s2.length())
      {
       t1=false;
      }      
      else
      {
        char ch1[]=s1.toLowerCase().toCharArray();
        char ch2[]=s2.toLowerCase().toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        t1=Arrays.equals(ch1,ch2);
      }
      if(t1)
      {
        System.out.println("two strings are anagrams");
      }
      else{
        System.out.println("two strigs are not anagrams");
      }
    }
}
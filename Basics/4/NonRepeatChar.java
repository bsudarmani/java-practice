import java.util.*;
import java.io.*;
class NonRepeatChar
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the string");
     String str=sc.next();
     char str1[]=str.toCharArray();
     boolean t1=true;
    for(char ch:str1)
    {
        if(str.indexOf(ch)==str.lastIndexOf(ch))
        {
            System.out.println("first non-repeating char: "+ ch);
            t1=false;
            break;
        }
    }
    if(t1)
    {
        System.out.println("There is non repeating char in string");
    }
    }
}
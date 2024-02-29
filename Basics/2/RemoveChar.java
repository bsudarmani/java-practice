import java.util.*;
import java.io.*;
class RemoveChar
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the string");
        String str=sc.next();
        // str=str.toLowerCase();
        System.out.println("Enter the char");
        char ch=sc.next().charAt(0);
        char chlow= Character.toLowerCase(ch);
        char chupp= Character.toUpperCase(ch);
        char charr[] = str.toCharArray();
        int j=0,count=0;
        for(int i=0;i<str.length();i++)
        {
            if(charr[i]!=chlow && charr[i]!=chupp)
            {
              charr[j++]=charr[i];
            }
            else
            {
                count++;
            }
        }
        while(count>0)
        {
          charr[j++]='\0';
          count--;
        }
       System.out.println(charr);
  
    }
}
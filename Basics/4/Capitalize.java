import java.util.*;
import java.io.*;
class Capitalize
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("enter the string:");
     String str=sc.nextLine();
     String  arr[]=str.split("\\s");
     String  capitalizeString="";
     for(String arr2:arr)
     {
        String firststr=arr2.substring(0,1).toUpperCase();
        String laststr=arr2.substring(1);
       capitalizeString+=firststr +laststr+ " ";
     }
     System.out.println(capitalizeString);
    }
}
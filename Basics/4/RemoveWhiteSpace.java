import java.util.*;
import java.io.*;
class RemoveWhiteSpace
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter the string:");
  String str=sc.nextLine();
  System.out.println("original string : "+str);
  str=str.replaceAll("\\s","");
  System.out.println("remove white spaces : "+str);
 }
}
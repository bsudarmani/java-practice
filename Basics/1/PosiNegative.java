import java.util.*;
import java.io.*;
class PosiNegative
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter a number");
  double num=sc.nextDouble();
  if(num>0)
  {
   System.out.println(num + " is positive");
  }
  else if(num<0)
  {
   System.out.println(num + " is negative ");
  }
  else
 {
  System.out.println(num + " is zero");
 }
 }
}
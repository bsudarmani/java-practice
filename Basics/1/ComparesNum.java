import java.util.*;
import java.io.*;
class ComparesNum
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("enter num1");
  int num1=sc.nextInt();
  System.out.println("enter num2");
  int num2=sc.nextInt();
  if(num1>num2)
  {
  System.out.println(num1 + " is greater than " + num2);
  }
   else if(num1<num2)
  {
  System.out.println(num1 + " is less than " + num2);
  }
  else if(num1==num2)
  {
  System.out.println(num1 + "  equal to " + num2 );
  }

 }
}
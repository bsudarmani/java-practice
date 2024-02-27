import java.util.*;
import java.io.*;
class Numbercheck
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter the number");
  int num=sc.nextInt();
  if(num>=1 && num<=100)
  {
    if(num>=1 && num<=50)
    {
    System.out.println("The number is in the lower half");
    }
    else
    {
    System.out.println("The number is in the upper half");
    }
   }
  else
  {
  System.out.println("Invalid number");
  }
}
}
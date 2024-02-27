import java.util.*;
import java.io.*;
class MultiplicationTable
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("enter the range of multiplication table");
  int num=sc.nextInt();
  System.out.println("enter the  number of multiplication table");
  int tnum=sc.nextInt();
 for(int i=0;i<=num;i++)
 {
 System.out.println(tnum + " * " + i + " = " + (tnum*i));
 }
 }
}
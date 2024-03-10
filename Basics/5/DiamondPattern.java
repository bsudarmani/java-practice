import java.util.*;
import java.io.*;
class DiamondPattern
{
 public static void main(String args[])
 {
  int r=5;
  int c=5;
  int sp=5;
  for(int i=1;i<=5;i++)
  {
  for(int k=1;k<=sp;k++)
   { 
   System.out.print(" ");
   }
   sp--;
   for(int j=1;j<=i;j++)
   {
    System.out.print("* ");
   }
  System.out.println();
  } 
   sp=5;
  for(int i=5;i>0;i--)
  {
   for(int k=5;k<=sp;k++)
   {
   System.out.print(" "); 
   }
   sp++;
   for(int j=1;j<=i;j++)
   {
    System.out.print("* ");
   }
  System.out.println();
  }
  }
 }
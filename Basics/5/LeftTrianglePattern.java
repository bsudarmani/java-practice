import java.util.*;
import java.io.*;
class LeftTrianglePattern
{
 public static void main(String args[])
 {
  int r=5;
  int c=5;
  int sp=4;
  for(int i=1;i<=5;i++)
  {
  for(int k=0;k<=sp;k++)
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
 }
}
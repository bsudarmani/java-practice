import java.util.*;
import java.io.*;
class HollowDiamondPattern
{
 public static void main(String args[])
 {
  int rows=4;
  for(int i=1;i<=rows;i++)
  { 
   for(int k=1;k<=rows-i;k++)
   {
   System.out.print(" ");
   }
   for(int j=1;j<=i*2-1;j++)
   {
   if(j==1 || j==i*2-1)
    {
     System.out.print("*");
    }
    else
    {
   System.out.print(" ");
    }
   }
  System.out.println();
  }
  for(int i=rows-1;i>0;i--)
  {
   for(int k=1;k<=rows-i;k++)
   {
   System.out.print(" ");
   }
   for(int j=1;j<=i*2-1;j++)
   {
   if(j==1 || j==i*2-1)
    {
     System.out.print("*");
    }
    else
    {
   System.out.print(" ");
    }
   }
  System.out.println();
  }
 }
} 
import java.util.*;
import java.io.*;
class HollowSquarePattern
{
 public static void main(String args[])
 {
  int r=5; 
  int c=5;
  for(int i=1;i<=r;i++)
  {
   for(int j=1;j<=c;j++)
   {
    if(i==5 || j==5 || i==1 || j==1)
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
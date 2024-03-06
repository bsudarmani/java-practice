import java.util.*;
import java.io.*;
class SumMatrices
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number of rows:");
     int r=sc.nextInt();
     System.out.println("Enter the number of columns:");
     int c=sc.nextInt();
     int arr1[][]=new int[r][c];
     int arr2[][]=new int[r][c];
     int sum[][]=new int[r][c];
    System.out.println("Enter the number of rows and columns 1st matrix:");
     for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        arr1[i][j]=sc.nextInt();
      }
     }
   System.out.println("Enter the number of rows and columns 2nd matrix:");
     for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        arr2[i][j]=sc.nextInt();
      }
     }
     System.out.println("sum of two matrix:");
    for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        sum[i][j]=arr1[i][j]+arr2[i][j];

      }
     }
      for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
       System.out.print(sum[i][j]+ "\t");
      }
      System.out.println();
     }
    }
}
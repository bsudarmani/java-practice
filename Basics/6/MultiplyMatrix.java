import java.util.*;
import java.io.*;
class MultiplyMatrix
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
     int arr3[][]=new int[r][c];
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
     System.out.println("multiply of two matrix:");
    for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        arr3[i][j]=0;
        for(int k=0;k<arr3.length;k++)
        {
        arr3[i][j]+=arr1[i][k]*arr2[k][j];
        }
      }
     }
      for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
       System.out.print(arr3[i][j]+ "\t");
      }
      System.out.println();
     }
    }
}
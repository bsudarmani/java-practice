import java.util.*;
import java.io.*;
class TransposeMatrix
{
    public static void main(String args[])
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number of rows:");
     int r=sc.nextInt();
     System.out.println("Enter the number of columns:");
     int c=sc.nextInt();
     int arr1[][]=new int[r][c];
     int transpose[][]=new int[r][c];
    System.out.println("Enter the number of rows and columns matrix:");
     for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        arr1[i][j]=sc.nextInt();
      }
     }
    for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
        transpose[i][j]=arr1[j][i];
      }
     }
    System.out.println("original matrix :");
    for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
       System.out.print(arr1[i][j]+ "\t");
      }
      System.out.println();
     }
   System.out.println("transpose of matrix :");
    for(int i=0;i<r;i++)
     {  
      for(int j=0;j<c;j++)
      {
       System.out.print(transpose[i][j]+ "\t");
      }
      System.out.println();
     }
    }
}
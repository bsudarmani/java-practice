import java.util.*;
import java.io.*;
class DistinctNumber
{
    public static void main(String args[])
    {
      Scanner sc=new Scanner(System.in);
     System.out.println("Enter number in array");
      int num=sc.nextInt();
      int arr[]=new int[num];
      System.out.println("Enter the array element");
      for(int i=0;i<arr.length;i++)
      {
        arr[i]=sc.nextInt();
      }
      
      
for (int i = 0; i <arr.length; i++) {
    boolean t1 = false;
    for (int j = 0; j < arr.length; j++) {
        if (i != j && arr[i] ==  arr[j]) {
            t1 = true;
            break;
        }
    }
    if (! t1) {
        System.out.println(arr[i]);
    }
    else
      {
        System.out.println("");
      }
}
    }    
    }

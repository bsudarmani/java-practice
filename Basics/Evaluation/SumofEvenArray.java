import java.util.*;
import java.io.*;
public class SumofEvenArray
{
 public static void main(String[] args)
 {
  int number[]={10,20,40,60,9,5,7};
  int sum=calculatesum(number);
  System.out.println("sum of array :"+sum);  
 }  
 public static int calculatesum(int arr[])
 {
    int sum=0;
    for(int arr1:arr)
    {
        if(arr1%2==0)
        {
            sum+=arr1;
        }
    }
    return sum;
 } 
}

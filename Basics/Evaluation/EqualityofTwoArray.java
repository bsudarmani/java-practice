import java.util.*;
import java.io.*;
public class EqualityofTwoArray
{
    public static void main(String[] args)
     {
        int arr1[]={10,20,30,40,50};
        int arr2[]={10,20,30,40,50};
        System.out.println("Array 1 :" + Arrays.toString(arr1));
        System.out.println("Array 2 :"+ Arrays.toString(arr2));
        equalstwoarray(arr1,arr2);
    }
    public static void equalstwoarray(int arr1[],int arr2[])
    {
        boolean  equal=true;
        if(arr1.length==arr2.length)
        {
          for(int i=0;i<arr1.length;i++)
          {
            if(arr1[i]!=arr2[i])
            {
                equal=false;
            }
          }
        }
        else
        {
            equal=false;
        }
        if(equal)
        {
            System.out.println("two arrays are equal");
        }
        else
        {
            System.out.println("two arrays are not equal");
        }
    } 
}

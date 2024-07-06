import java.io.*;
import java.util.*;
public class CommonElement 
{
  public static void main(String[] args)
  {
    int num1[]={1,2,4,5};
    int num2[]={2,4,5,1};
    System.out.println("num1 array "+Arrays.toString(num1));
    System.out.println("num2 array "+Arrays.toString(num2));
    for(int i=0;i<num1.length;i++)
    {
        for(int j=0;j<num2.length;j++)
        {
            if(num1[i]==(num2[j]))
            {
                System.out.println("common element:"+num1[i]);
            }   
        }
    }
  }   
}

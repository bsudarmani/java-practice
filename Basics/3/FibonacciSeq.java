import java.util.*;
import java.io.*;
class FibonacciSeq
{
    public static void main(String args[])
    {
    int num=10;
    System.out.println("Enter the number is "+num);
    int s1=0,s2=1,s3=0;
    System.out.println(s1 + " "+ s2);
    for(int i=0;i<num;i++)
    {
         s3=s1+s2;
        System.out.println(s3);
        s1=s2;
        s2=s3;
    }
    }
}

import java.io.*;
import java.util.*;
public class MultiplicationTable 
{
 public static void main(String[] args) 
 {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter an Integer ");
    int num=sc.nextInt();
    System.out.println("Multiplication table for :" + num);
    for(int i=1;i<=10;i++)
    {
        System.out.println(i+ " X " + num + " = " + (i*num));
    }
 }    
}

import java.util.*;
import java.io.*;
public class Swapping
{
 public static void main(String[] args) 
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("enter 1st number");
  int num1=sc.nextInt();
  System.out.println("enter 2nd number");
  int num2=sc.nextInt();
  System.out.println("Before swapping:");
  System.out.println("First number: " + num1);
  System.out.println("Second number: " + num2);  
  num1=num1+num2;
  num2=num1-num2;
  num1=num1-num2;
  System.out.println("After swapping:");
  System.out.println("First number: " + num1);
  System.out.println("Second number: " + num2);  
 }   
}

import java.util.*;
import java.io.*;
public class CalculateUser 
{
 public static void main(String[] args) 
 {
    Scanner sc=new Scanner(System.in);
  System.out.println("Enter the meters ");   
  double meters=sc.nextDouble();
  double feet = meters * 3.28084; 
  double inchs = feet * 12; 
  double cmeters = meters * 100;
  System.out.println("convert feet "+ feet);
  System.out.println("convert inchs "+inchs);
  System.out.println("convert cmeters "+cmeters);
 }    
}
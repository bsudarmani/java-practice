import java.util.*;
import java.io.*;
class Temperature
{
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("enter a temperaturein Celsius");
 Double celsius=sc.nextDouble();
 Double fahrenheit= (celsius * 9/5) + 32;
 System.out.println(fahrenheit);
 }
}
import java.util.*;
import java.time.*;
public class CalculateBirthYear 
{
 public static void main(String[] args) 
 {
     System.out.println("Enter your age");
     Scanner sc=new Scanner(System.in);
     int age=sc.nextInt();
     int currentyear=LocalDate.now().getYear();
     int birthyear=currentyear-age;
     System.out.println("Birthday year"+birthyear);
 }   
}

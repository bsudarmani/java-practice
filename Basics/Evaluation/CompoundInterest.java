import java.util.*;
public class CompoundInterest
{
    public static void main(String[] args)
    {
     Scanner sc=new Scanner(System.in);
     System.out.println("Enter principal amount");
     double principal=sc.nextDouble();
     System.out.println("Enter the interest rate ");
     double rate=sc.nextDouble()/100;
     System.out.println("Enter the year");
     double year=sc.nextDouble();
     double amount = principal * Math.pow(1 + rate, year);  
     double interest = amount - principal; 
     System.out.println("Compound interest after " + year + " years: " + interest);
    }
}
import java.io.*;
import java.util.*;
public class CalculateArea 
{
    public static void main(String[] args)
     {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the radius");
        double radius=sc.nextDouble();
        double area=Math.PI*radius*radius;
        System.out.println("Area of circle: "+area);
    }
}

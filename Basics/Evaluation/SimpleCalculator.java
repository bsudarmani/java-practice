import java.lang.*;
import java.util.*;
import java.io.*;

class SimpleCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the 1st number");
        double num1 = sc.nextDouble();
        System.out.println("Enter the 2nd number");
        double num2 = sc.nextDouble();
        System.out.println("Perform basic arithmetic operations");
        System.out.println("1.addition");
        System.out.println("2.subtraction");
        System.out.println("3.multiplication");
        System.out.println("4.division");
        System.out.println("select the operation");
        int select = sc.nextInt();
        switch (select) {
            case 1:
                double add = num1 + num2;
                System.out.println("addition of two numbers:" + add);
                break;
            case 2:
                double sub = num1 - num2;
                System.out.println("subtraction of two numbers:" + sub);
                break;
            case 3:
                double mul = num1 * num2;
                System.out.println("multiplication of two numbers:" + mul);
                break;
            case 4:
                if (num2 == 0) {
                    System.out.println("Error: Division by zero");
                } else {
                    double div = num1 / num2;
                    System.out.println("division of two numbers " + div);
                }
                break;
            default:
                System.out.println("Invalid choice");
        }
    }
}
import java.util.*;
import java.io.*;
public class FactorialRecursion 
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number:");
        int num=sc.nextInt();
        int fact=check(num);
        System.out.println("factorial of given number:"+fact);
    }
    public static int check(int n1)
    {
        if(n1== 0 || n1==1)
        {
            return 1;
        }
        return n1*check(n1-1);
    }
}

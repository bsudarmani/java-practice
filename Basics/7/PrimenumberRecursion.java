import java.util.Scanner;

import org.omg.CORBA.SystemException;
class PrimenumberRecursion
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number");
        int num=sc.nextInt();
        boolean t1=checkprime(num,2);
        if(t1)
        {
            System.out.println("Number is prime");
        }
        else
        {
            System.out.println("Number is not prime");
        }
    }
    public static boolean checkprime(int n1,int div)
    {
        if (n1<= 2) {
            return (n1==2) ? true : false;
        }
        if (n1 %div == 0) {
            return false;
        }
        if (div * div > n1) {
            return true;
        }
        return checkprime(n1, div+ 1);
    }
}
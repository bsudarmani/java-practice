import java.util.*;
public class NprimeNumber 
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number");
        int num=sc.nextInt();
        for(int i=1;i<=num;i++)
        {
            boolean t1=prime(i);
            if(t1)
            {
                System.out.println(i + " ");
            }
        }
    }
    public static boolean prime(int n1)
    {
     if(n1==0 || n1==1)
     {
        return false;
     }
     for(int i=2;i<n1;i++)
     {
        if(n1%i==0)
        {
            return false;
        }
     }
     return true;
    }
}

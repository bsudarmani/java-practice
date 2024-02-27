import java.util.*;
import java.util.*;
class ThirdLargest
{
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 System.out.println("Enter number in array");
 int n=sc.nextInt();
 int number[]=new int[n];
 System.out.println("Enter the number");
 for(int i=0;i<n;i++)
 {
 number[i]=sc.nextInt();
 }
 Arrays.sort(number);
 if(number.length<3)
 {
 System.out.println("-1");
 }
else
 {
 System.out.println(number[number.length-3]);
 }
}
}
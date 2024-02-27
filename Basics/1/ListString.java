import java.util.*;
import java.io.*;
class ListString
{
 public static void main(String args[])
 {
  Scanner sc=new Scanner(System.in);
  System.out.println("Enter the name of string");
  int num=sc.nextInt();
  String arr[]=new String[num];
 System.out.println("list of Names");
 for(int i=0;i<num;i++)
 {
 arr[i]=sc.next();
 }
 Arrays.sort(arr);
 System.out.println("sorted Names:");
 for(String str:arr)
 System.out.println(str);
 }
}

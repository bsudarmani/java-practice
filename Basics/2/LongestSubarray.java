import java.util.*;
import java.io.*;
class LongestSubarray
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the no of array");
        int num=sc.nextInt();
        int number[]=new int[num];
        System.out.println("enter the number in array");
        for(int i=0;i<number.length;i++)
        {
            number[i]=sc.nextInt();
        }
        int maxlen = 1;
        int currentlen = 1;
        int endIndex = 0;
        int currentendIndex = 0;

        for (int i = 1; i < number.length; i++) {
            if (number[i] > number[i - 1]) {
                currentlen++;
                if (currentlen > maxlen) {
                    maxlen = currentlen;
                    endIndex = i;
                }
            } else {
                currentlen = 1;
                currentendIndex = i;
            }
        }
        for (int i = endIndex - maxlen + 1; i <= endIndex; i++) {
            System.out.print(number[i]);
        }
    }
}
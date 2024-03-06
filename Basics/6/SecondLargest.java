import java.util.*;
import java.io.*;
 class SecondLargest
{    
    public static int SecondLargest(int[] arr) {
        int firstLar = arr[0];
        int secondLar = arr[0];
        for (int num : arr) {
            if (num > firstLar) {
                secondLar = firstLar;
                firstLar = num;
            } else if (num > secondLar && num != firstLar) {
                secondLar = num;
            }
        }
        
        return secondLar;
    }
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number in array : ");
        int num=sc.nextInt();    
        int  number[]=new int[num];
        System.out.println("enter the number one by one : ");
        for(int i=0;i<number.length;i++)
        {
            number[i]=sc.nextInt();
        }
        int secondLargest = SecondLargest(number);
        
        System.out.println("Second largest element in the array: " + secondLargest);
    }
}

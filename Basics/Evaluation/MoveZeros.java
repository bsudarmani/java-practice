import java.util.*;
import  java.io.*;
public class MoveZeros
{
 public static void main(String[] args)
 {
    int nums[] = {3,6,2,3,0,1,2,5,0,5,6};
    int i = 0;
    System.out.println("Original array:");
    for (int num: nums)
        System.out.print(num + "  ");
    for (int j = 0, l = nums.length; j < l;) {
        if (nums[j] == 0)
            j++;
        else {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j++;
        }
    }
    while (i <nums.length)
        nums[i++] = 0;
    System.out.println("\nAfter array");
    for (int n : nums)
        System.out.print(n + "  ");
    System.out.print("\n");  
 }   
}

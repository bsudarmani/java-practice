import java.util.*;
import java.io.*;
    public class LongestSequence 
     {    
    public static void main(String[] args)
     {
        int nums[]= {49, 1, 3, 200, 2, 4, 70, 5};  
        System.out.println("Original array length: " + nums.length);
        System.out.println("Array:"+Arrays.toString(nums));
        System.out.println("The After Array: " + checksequence(nums));   
    }
    public static int checksequence(int[] nums) {
         HashSet hs = new HashSet();
        for (int i : nums) {
            hs.add(i);
        }
        int len = 0;
        for (int i : nums) {
            int length = 1;
            for (int j = i - 1; hs.contains(j); --j) {
                hs.remove(j);
                ++length;
            }
            for (int j = i + 1; hs.contains(j); ++j) {
                hs.remove(j);
                ++length;
            }
            len = Math.max(len, length);
        }
        return len;
    }
}


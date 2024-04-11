import java.util.*;
import java.io.*;
 public class SubsetRecursion
 {
    public static void main(String[] args) {
        char[] set = {'a', 'b', 'c'};
        int n = set.length;
        generateSubsets(set, 0, n, "");
    }
    public static void generateSubsets(char[] set, int index, int n, String subset) {
        if (index == n) {
            System.out.println(subset);
            return;
        }
        generateSubsets(set, index + 1, n, subset + set[index]);
        generateSubsets(set, index + 1, n, subset);
    }
} 
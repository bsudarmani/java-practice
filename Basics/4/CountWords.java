import java.util.*;
import java.io.*;
 class CountWords {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string: ");
        String Str = scanner.nextLine();
        int count = countWords(Str);
        System.out.println("Number of words in a string: " + count);
    }

    public static int countWords(String str) {
        if (str == null || str.isEmpty()) {
            return 0;
        }
        String[] words = str.split("\\s+");
        return words.length;
    }
}
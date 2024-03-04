import java.util.*;
import java.io.*;
 class LengthSubString 
{
static void longestSubstring(String inputString)
 {
       char[] arr1 = inputString.toCharArray();
        String longestSubstring = "";
        int maxLength = 0;
        LinkedHashMap<Character, Integer> charPosMap = new LinkedHashMap<>();
        for (int i = 0; i < arr1.length; i++) 
        {
            char ch = arr1[i];
            if (!charPosMap.containsKey(ch))
            {
                charPosMap.put(ch, i);
            } else
            {
                i = charPosMap.get(ch);
                charPosMap.clear();
            }
            if (charPosMap.size() > maxLength)
            {
                maxLength = charPosMap.size();
                longestSubstring = inputString.substring(i - maxLength + 1, i + 1);
            }
        }
        System.out.println("The longest Substring Length: " + maxLength);
    }
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the string :");
         String str=sc.nextLine();
        longestSubstring(str);
    }
}

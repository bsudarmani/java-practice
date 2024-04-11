import java.util.*;
public class PermutationRecursion
{
  public static List < String > generatePermutations(String str) {
    List < String > permutations = new ArrayList < > ();
    generatePermutationsHelper(str, "", permutations);
    return permutations;
  }

  private static void generatePermutationsHelper(String str, String current, List < String > permutations) {
    if (str.isEmpty()) {
      permutations.add(current);
      return;
    }
    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);
      String remaining = str.substring(0, i) + str.substring(i + 1);
      generatePermutationsHelper(remaining, current + ch, permutations);
    }
  }

  public static void main(String[] args)
   {
    Scanner sc=new Scanner(System.in);
    System.out.println("enter the string");
    String input = sc.next();
    List < String > permutations = generatePermutations(input);
    for (String permutation: permutations) {
      System.out.println(permutation);
    }
  }
}

import java.util.Scanner;

public class FindSum{
    public static void main(String[] args)
     {
      Scanner sc=new Scanner(System.in);
     System.out.println("Enter the number in array:");
     int num=sc.nextInt();
     int number[]=new int[num];
     System.out.println("Enter the number in one by one");
     for(int i=0;i<num;i++)
     {  
     number[i]=sc.nextInt();
     }
       System.out.println("Enter target value:");
       int target=sc.nextInt();
        checksum(number, target);
    }

    public static void checksum(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] + array[j] == target) {
                    System.out.println("The sum of index " + i + " and " + j + " equals the target value.");
                    System.out.println("Values: " + array[i] + ", " + array[j]);
                    return;
                }
            }
        }
    }
}
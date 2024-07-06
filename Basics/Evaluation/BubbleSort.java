public class BubbleSort { 
     public static void main(String args[]) 
     {
        String[] arr = {"banu","mani","sudar","anu","raju"};
        System.out.println("Array before sorting:");
        printArray(arr);
        bubbleSort(arr);
        System.out.println("\nArray after sorting:");
        printArray(arr);
    }
    public static void bubbleSort(String[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j].compareTo(arr[j + 1]) > 0) {
                    String temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    public static void printArray(String[] arr) {
        for (String s : arr) {
            System.out.print(s + " ");
        }
    }
}
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Problem 4: Generating Even Squares
public class Problem4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // list of integers
        System.out.println("Enter a list of integers (space-separated):");
        String[] input = scanner.nextLine().split(" ");
        List<Integer> numbers = new ArrayList<>();
        for (String num : input) {
            numbers.add(Integer.parseInt(num));
        }

        // to generate a new list of squares of even numbers
        List<Integer> evenSquares = generateEvenSquares(numbers);
        System.out.println("List of squares of even numbers:");
        System.out.println(evenSquares);

        // to take start and end indices for slicing the list
        System.out.print("Enter the start index: ");
        int startIndex = scanner.nextInt();
        System.out.print("Enter the end index: ");
        int endIndex = scanner.nextInt();
        // Example
        // Enter a list of integers (space-separated):
        // 1 2 3 4 5 6 7 8 9 10
        // Enter the start index:
        // 2
        // Enter the end index:
        // 5

        // sublist
        List<Integer> sublist = sliceList(numbers, startIndex, endIndex);
        System.out.println("Sublist from index " + startIndex + " to " + endIndex + ":"); //need to check this again
        System.out.println(sublist);

        scanner.close();
    }

    // to generate a new list of squares
    public static List<Integer> generateEvenSquares(List<Integer> numbers) {
        List<Integer> evenSquares = new ArrayList<>();
        for (int number : numbers) {
            if (number % 2 == 0) {
                evenSquares.add(number * number);
            }
        }
        return evenSquares;
    }

    // to extract a sublist from the original list
    public static List<Integer> sliceList(List<Integer> numbers, int startIndex, int endIndex) {
        // Validate indices
        if (startIndex < 0 || endIndex >= numbers.size() || startIndex > endIndex) {
            System.out.println("Invalid indices. Returning an empty list.");
            return new ArrayList<>();
        }
        return numbers.subList(startIndex, endIndex + 1);
        // Output:
        // List of squares of even numbers:
        //[4, 16, 36]
        //Sublist from index 2 to 5:
        //[3, 4, 5, 6]
    }
}
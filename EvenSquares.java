import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class EvenSquares {

    public static List<Integer> getEvenSquares(List<Integer> list) {
        return list.stream()
                   .filter(n -> n % 2 == 0)
                   .map(n -> n * n)
                   .collect(Collectors.toList());
    }

    public static List<Integer> getSublist(List<Integer> list, int start, int end) {
        // Ensure start and end indices are within bounds
        if (start < 0) start = 0;
        if (end > list.size()) end = list.size();
        if (start > end) start = end;
        return list.subList(start, end);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the list of integers (in the format [1, 2, 3, 4, 5]):");
        String input = scanner.nextLine().trim();
        
        if (input.startsWith("[") && input.endsWith("]")) {
            input = input.substring(1, input.length() - 1);
        }
        
        String[] inputArray = input.split(",");
        List<Integer> numbers = new ArrayList<>();
        for (String s : inputArray) {
            try {
                numbers.add(Integer.parseInt(s.trim()));
            } catch (NumberFormatException e) {
                System.out.println("Invalid number format: " + s.trim());
            }
        }

        List<Integer> evenSquares = getEvenSquares(numbers);
        
        System.out.println("Enter start index for sublist:");
        int start = scanner.nextInt();
        System.out.println("Enter end index for sublist:");
        int end = scanner.nextInt();
        
        List<Integer> sublist = getSublist(numbers, start, end);

        System.out.println("----------------------");
        System.out.println("List of squares of even numbers: " + evenSquares);
        System.out.println("Sublist: " + sublist);

        scanner.close();
    }
}
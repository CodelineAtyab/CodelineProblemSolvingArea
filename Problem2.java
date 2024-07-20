import java.util.Scanner;
import java.util.Stack;
// Problem 2: Convert Decimal to Binary
public class Problem2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("## Enter a positive decimal numbers ONLY ##");
        // iinput form user
        System.out.print("Input: ");
        int decimalNumber = scanner.nextInt();

        // to check if the number is positive
        if (decimalNumber < 0) {
            System.out.println("Please enter a positive number.");
            return;
        }

        String binaryNumber = convertDecimalToBinary(decimalNumber);

        System.out.println("Output: "+ binaryNumber);
    }
    // to convert a positive decimal number to its binary equivalent
    public static String convertDecimalToBinary(int decimalNumber) {
        // if the number is 0, return 0
        if (decimalNumber == 0) {
            return "0";
        }

        Stack<Integer> stack = new Stack<>();

        // if number greater than 0
        while (decimalNumber > 0) {
            int remainder = decimalNumber % 2;
            stack.push(remainder);
            decimalNumber = decimalNumber / 2;
        }

        // Create a string to store the binary equivalent
        StringBuilder binaryNumber = new StringBuilder();

        // Pop the stack to get the binary equivalent
        while (!stack.isEmpty()) {
            binaryNumber.append(stack.pop());
        }

        return binaryNumber.toString();
    }
}
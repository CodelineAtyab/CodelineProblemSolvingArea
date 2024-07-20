import java.util.Scanner;

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

        //String binaryNumber = convertDecimalToBinary(decimalNumber);

        //System.out.println("Output: "+ binaryNumber);
    }

}
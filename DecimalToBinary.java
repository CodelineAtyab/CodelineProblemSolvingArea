import java.util.Scanner;

public class DecimalToBinary {

    public static String convertToBinary(int decimal) {
        if (decimal == 0) return "0";
        StringBuilder binary = new StringBuilder();
        while (decimal > 0) {
            binary.insert(0, decimal % 2);
            decimal = decimal / 2;
        }
        return binary.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input: ");
        int decimal = scanner.nextInt();

        if (decimal < 0) {
            System.out.println("Error: Negative numbers are not allowed.");
        } else {
            String binary = convertToBinary(decimal);
            System.out.println("Output: " + binary);
        }
        
        scanner.close();
    }
}

import java.util.Scanner;

public class TriangleDisplay {

    public static void printRightAngledTriangle(int rows) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("1 ");
            }
            System.out.println();
        }
    }

    public static void printPalindromicTriangle(int rows) {
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }
            System.out.println();
        }
    }

    public static void printHelp() {
        System.out.println("Help:");
        System.out.println("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrore.");
        System.out.println("The first few lines of a Palindromic Triangle are:");
        System.out.println("1");
        System.out.println("11");
        System.out.println("121");
        System.out.println("12321");
        System.out.println("1234321");
        System.out.println("You can use this pattern to draw a Palindromic Triangle for any number of lines.");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice = 0;

        do {
            System.out.println("Menu:");
            System.out.println("1. Display a right-angle triangle of ones");
            System.out.println("2. Display a Palindromic Triangle");
            System.out.println("3. Help");
            System.out.println("4. Exit");
            System.out.println("----------------------");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            if (choice == 1 || choice == 2) {
                System.out.print("Enter number of rows: ");
                int rows = scanner.nextInt();

                switch (choice) {
                    case 1:
                        System.out.println("----------------------");
                        printRightAngledTriangle(rows);
                        System.out.println("----------------------");
                        break;
                    case 2:
                        System.out.println("----------------------");
                        printPalindromicTriangle(rows);
                        System.out.println("----------------------");
                        break;
                }
            } else if (choice == 3) {
                System.out.println("----------------------");
                printHelp();
                System.out.println("----------------------");
            } else if (choice == 4) {
                System.out.println("Exiting the program.");
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);

        scanner.close();
    }
}

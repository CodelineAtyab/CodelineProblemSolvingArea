import java.util.Scanner;

//Problem 3: Interactive Triangle Display
public class Problem3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            // Display the menu
            System.out.println("___  ___  ____ __  __ __ __\r\n" + //
                                "||\\\\//|| ||    ||\\ || || ||\r\n" + //
                                "|| \\/ || ||==  ||\\\\|| || ||\r\n" + //
                                "||    || ||___ || \\|| \\\\_//");
            System.out.println("\n1. Display a right-angle triangle of ones");
            System.out.println("2. Display a palindromic triangle");
            System.out.println("3. Help");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    // right-angle triangle of ones
                    System.out.print("Enter the number of lines: ");
                    int lines = scanner.nextInt();
                    displayRightAngleTriangle(lines);
                    break;

                case 2:
                    // palindromic triangle
                    System.out.print("Enter the number of lines: ");
                    lines = scanner.nextInt();
                    displayPalindromicTriangle(lines);
                    break;

                case 3:
                    // help information
                    displayHelp();
                    break;

                case 4:
                    // Exiting 
                    System.out.println("Exiting the program......");
                    break;

                default:
                    System.out.println("Invalid choice. Please enter a number from 1 to 4.");
            }
        } while (choice != 4);

        scanner.close();
    }

    // to display a right-angle triangle of ones
    public static void displayRightAngleTriangle(int lines) {
        for (int i = 1; i <= lines; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("1");
            }
            System.out.println();
        }
    }

    // to display a palindromic triangle
    public static void displayPalindromicTriangle(int lines) {
        for (int i = 1; i <= lines; i++) {
            // left 
            for (int j = 1; j <= i; j++) {
                System.out.print(j);
            }

            // right
            for (int j = i - 1; j >= 1; j--) {
                System.out.print(j);
            }

            System.out.println();
        }
    }


    // to display help information
    public static void displayHelp() {
        System.out.println(" _   _      _                                               \r\n" + //
                        "| | | | ___| |_ __                                          \r\n" + //
                        "| |_| |/ _ \\ | '_ \\                                         \r\n" + //
                        "|  _  |  __/ | |_) |                                        \r\n" + //
                        "|_| |_|\\___|_| .__/                                         \r\n" + //
                        " ___        _|_|                          _   _             \r\n" + //
                        "|_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  \r\n" + //
                        " | || '_ \\| |_ / _ \\| '__| '_ ` _ \\ / _` | __| |/ _ \\| '_ \\ \r\n" + //
                        " | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | |\r\n" + //
                        "|___|_| |_|_|  \\___/|_|  |_| |_| |_|\\__,_|\\__|_|\\___/|_| |_|");


        System.out.println("\n\n1. Display a right-angle triangle of ones:");
        System.out.println("   - This option will prompt you to enter the number of lines.");
        System.out.println("   - It will then print a right-angle triangle consisting of ones.");
        System.out.println("   Example:");
        System.out.println("   Enter your choice: 1");
        System.out.println("   Enter the number of lines: 4");
        System.out.println("   Output:");
        System.out.println("   1");
        System.out.println("   11");
        System.out.println("   111");
        System.out.println("   1111");
        System.out.println();
        
        System.out.println("2. Display a palindromic triangle:");
        System.out.println("   - This option will prompt you to enter the number of lines.");
        System.out.println("   - It will then print a palindromic triangle.");
        System.out.println("   Example:");
        System.out.println("   Enter your choice: 2");
        System.out.println("   Enter the number of lines: 4");
        System.out.println("   Output:");
        System.out.println("   1");
        System.out.println("   121");
        System.out.println("   12321");
        System.out.println("   1234321");
        System.out.println();
        
        System.out.println("3. Display this help information:");
        System.out.println("   - This option displays information about how to use the program.");
        System.out.println("   - It explains each menu option in detail with examples.");
        System.out.println();
        
        System.out.println("4. Exit:");
        System.out.println("   - This option exits the program.");
    }
}

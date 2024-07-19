// Problem 1: User Login Validation

import java.util.Scanner;
import java.util.regex.Pattern;

public class Problem1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt for username input
        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        // Prompt for password input
        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        // Prompt for email input
        System.out.print("Enter email: ");
        String email = scanner.nextLine();

        // Validate username
        if (validateUsername(username)) {
            System.out.println("Username is valid.");
        } else {
            System.out.println("Username is invalid.");
        }

        // Validate password
        if (validatePassword(password)) {
            System.out.println("Password is valid.");
        } else {
            System.out.println("Password is invalid.");
        }

        // Validate email
        if (validateEmail(email)) {
            System.out.println("Email is valid.");
        } else {
            System.out.println("Email is invalid.");
        }
        
        scanner.close();
    }

    // Validate username method
    public static boolean validateUsername(String username) {
        if (username.isEmpty()) {
            return false;
        }
        if (username.length() > 50) {
            return false;
        }
        return true;
    }

    // Validate password method
    public static boolean validatePassword(String password) {
        if (password.length() < 8) {
            return false;
        }
        if (!Pattern.compile("[!@#$%^&*(),.?\":{}|<>]").matcher(password).find()) {
            return false;
        }
        if (!Pattern.compile("\\d").matcher(password).find()) {
            return false;
        }
        if (!Pattern.compile("[A-Z]").matcher(password).find()) {
            return false;
        }
        if (!Pattern.compile("[a-z]").matcher(password).find()) {
            return false;
        }
        return true;
    }

    // Validate email method 
    public static boolean validateEmail(String email) {
        if (!Pattern.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$").matcher(email).matches()) {
          
            return false;
        }
        return true;
    }
}

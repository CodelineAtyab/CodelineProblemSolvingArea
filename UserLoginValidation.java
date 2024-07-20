import java.util.Scanner;
import java.util.regex.Pattern;

public class UserLoginValidation {

    public static boolean validateUsername(String username) {
        return !username.isEmpty() && username.length() <= 50;
    }

    public static boolean validatePassword(String password) {
        if (password.length() < 8) return false;
        boolean hasSpecial = !password.matches("[A-Za-z0-9 ]*");
        boolean hasNumber = password.matches(".*\\d.*");
        boolean hasUpper = !password.equals(password.toLowerCase());
        boolean hasLower = !password.equals(password.toUpperCase());
        return hasSpecial && hasNumber && hasUpper && hasLower;
    }

    public static boolean validateEmail(String email) {
        String emailRegex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,6}$";
        Pattern pattern = Pattern.compile(emailRegex);
        return pattern.matcher(email).matches();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Username:");
        String username = scanner.nextLine();
        System.out.print("Enter Password:");
        String password = scanner.nextLine();
        System.out.print("Enter Email:");
        String email = scanner.nextLine();


        if (!validateUsername(username)) {
            System.out.println("UserName is Invalid.");
        }
        else
        {
           System.out.println("UserName is Valid."); 
        }
        if (!validatePassword(password)) {
            System.out.println("Password is Invalid.");
        }
        else
        {
           System.out.println("Password is Valid."); 
        }
        if (!validateEmail(email)) {
            System.out.println("Email is Invalid.");
        }
        else
        {
           System.out.println("Email is Valid."); 
        }

        scanner.close();
    }
}
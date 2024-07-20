import java.util.regex.*;
import java.util.*;
class GFG {
 
    public static String passwordRegex = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\\S+$).{8,}$";
    public static String emailRegex = "^[A-Za-z0-9+_.-]+@+[A-Za-z0-9]+(.)+[A-Za-z0-9]$";
    public static String usernameRegex = "^.{1,50}$";
    
    public static boolean isValid(String input, String regex){
        if (input == null) return false;
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(input);
        return m.matches();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        String user,pass,email;
        
        System.out.print("Enter the Username: ");  
        user = sc.nextLine(); 
        System.out.print("Enter the Password: ");
        pass = sc.nextLine();
        System.out.print("Enter the Email: ");
        email = sc.nextLine();
        
        if(isValid(user,usernameRegex)) {
            System.out.println("Username is valid");
        } else {
           System.out.println("Username is invalid");
        }
        
        if(isValid(pass,passwordRegex)) {
            System.out.println("Password is valid");
        } else {
           System.out.println("Password is invalid");
        }
        
        if(isValid(email,emailRegex)) {
            System.out.println("Email is valid");
        } else {
           System.out.println("Email is invalid");
        }
        
        
    }
}
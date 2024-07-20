import java.util.Scanner;

public class task3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        boolean flag = true;

        while(flag ){
            System.out.println("Menu:");
            System.out.println("1. Display a right-angle triangle of ones");
            System.out.println("2. Display a Palindromic Triangle");
            System.out.println("3. Help");
            System.out.println("4. Exit");
         
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            
            // right-angle triangle
            if (choice == 1) {
                System.out.print("Enter the number of lines: ");
                int rows = sc.nextInt();

                for(int i = 0; i < rows; i++){
                    for(int j = 0; j <= i; j++){
                        System.out.print("1");
                    }
                    System.out.println();
                }

                choice = 0;
            }
            
            // Palindromic Triangle
            else if (choice == 2 ){
                System.out.print("Enter the number of lines: ");
                int rows = sc.nextInt();

                for(int i = 1; i <= rows; i++){
                    for (int j = 1; j <= i; j++)
                        System.out.print(j);
                    for (int j = i - 1; j >= 1; j--)
                        System.out.print(j);

                    System.out.println();
                }

                choice = 0;
            }
            // Help
            else if (choice == 3 ){
                System.out.println("Help:");
        System.out.println("A Palindromic Triangle is a triangular array of numbers where each row forms a palindromic.");
        System.out.println("The first new lines of palindromic Triangule are: ");
                System.out.println("1");
                System.out.println("121");
                System.out.println("12321");
                System.out.println("1234321");
         System.out.println("You can use this pattern to draw a palindromic triangle for any number of lines. ");
            }
            // Exit
            else if (choice == 4 ){
                flag = false;
                System.out.println("Exiting the program.");
            }


        }
    }
}
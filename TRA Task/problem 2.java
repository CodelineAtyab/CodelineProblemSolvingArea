import java.util.Scanner;

public class task2 {
    public static void main(String args[]) {
      
        int D_num;
        int bin_num[] = new int[70];
        
        Scanner a = new Scanner(System.in);
            System.out.print("Enter a Decimal Number: ");
            D_num = a.nextInt();
           
            
           int Q = D_num;
           int i =1;
           while (Q != 0) {
           bin_num[i++] = Q % 2;
           Q = Q / 2;
           
           }
          System.out.print("Binary number is: ");
        for (int j = i - 1; j > 0; j--) {
        System.out.print(bin_num[j]);
        }
        System.out.print("\n");
    }
}
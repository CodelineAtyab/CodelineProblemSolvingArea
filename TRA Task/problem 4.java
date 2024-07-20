import java.util.Scanner;
class task4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("How many Integers in the list? ");
        int size = input.nextInt();
        int[] n = new int [size];
        System.out.println("Enter the list of integers:");
      
        for(int i =0; i<size ;i++)
            {
                n [i] = input.nextInt();
            }
            int i , j ;
            System.out.println("List of sequares of even numbers:"+ " ");
            for( i=0;i<n.length;i++){  
                if(n[i]%2==0){  
                 j = n[i] * n[i];
                System.out.println(j+" ");
                }
            }
          
    System.out.print("Enter start index:");
     Scanner a = new Scanner(System.in);
     int sta = a.nextInt();
    System.out.print("Enter end index:");
    Scanner e= new Scanner(System.in);
     int end = e.nextInt();
     System.out.print("sublist:");
     for (int l=sta; l< end ; l++)
     {
     System.out.print(n[l]+" ");
     }
	System.out.print("]");
}
}
        
    
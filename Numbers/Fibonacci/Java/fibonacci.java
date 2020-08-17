import java.util.Scanner;

public class fibonacci {

    public static void inputLimit()
    {
        // <input> -> digit
        System.out.println("\nEnter the number of Fibonacci sequence members you want to see: ");

        Scanner scanner = new Scanner(System.in);
        final int num = Integer.parseInt(scanner.nextLine());

        fib(num);

        System.out.println("\nEnter 'y' to continue: ");
        String answer = scanner.nextLine();

        if(answer.toLowerCase().equals("y"))
            inputLimit();
    }

    private static void fib(int N) {
        //  N -> fibonacci series
        long t1 = 0, t2 = 1, nextTerm = 0;

        for (int i = 1; i <= N; ++i)
        {
            if (i == 1)
            {
                System.out.print(t1 + " ");
                continue;
            }
            if (i == 2)
            {
                System.out.print(t2 + " ");
                continue;
            }
            nextTerm = t1 + t2;
            t1 = t2;
            t2 = nextTerm;

            System.out.print(nextTerm + " ");
        }
    }

    public static void main(String[] args)
    {
        // Main function
        // Get user's number
        // Calculate result
        // Print result
        
        System.out.println("-- Fibonacci series-- ");

        inputLimit();
    }
}

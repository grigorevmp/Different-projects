import java.util.Scanner;

public class factorial {

    private static String TOOGLE = "cycle";  // recursion

    public static void inputLimit()
    {
        // <input> -> digit
        System.out.println("\nInput number: ");

        Scanner scanner = new Scanner(System.in);
        final int num = Integer.parseInt(scanner.nextLine());

        System.out.println(fact(num));

        System.out.println("\nEnter 'y' to continue: ");
        String answer = scanner.nextLine();

        if(answer.toLowerCase().equals("y"))
            inputLimit();
    }

    private static int recur_factorial(int num) {
        if (num == 1)
            return num;
        else
            return num * recur_factorial(num - 1);
    }

    private static int fact(int num) {
        //  N -> factorial

        int result = 1;

        if (TOOGLE.equals("cycle")) {
            for (int i = 0; i < num; ++i)
                result *= (i + 1);
        }
        if (TOOGLE.equals("recursion")) {
            result = recur_factorial(num);
        }

        return result;

    }

    public static void main(String[] args)
    {
        // Main function
        // Get user's number
        // Calculate result
        // Print result

        System.out.println("-- Factorial -- ");

        inputLimit();
    }
}

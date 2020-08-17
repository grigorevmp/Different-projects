import java.util.Scanner;

public class prime {

    public static void inputLimit()
    {
        // <input> -> digit
        System.out.println("\nEnter the number to get it's prime factors: ");

        Scanner scanner = new Scanner(System.in);
        final int num = Integer.parseInt(scanner.nextLine());

        factorize(num);

        System.out.println("\nEnter 'y' to continue: ");
        String answer = scanner.nextLine();

        if(answer.toLowerCase().equals("y"))
            inputLimit();
    }

    private static void factorize(int num) {
        // num -> prime factors

        int pre = 0;
        while (num % 2 == 0) {
            if (pre != 2)
                System.out.print(2 + " ");
            num = num / 2;
            pre = 2;
        }

        for (int i = 3; i * i <= num; i = i + 2) {
            while (num % i == 0) {
                if (pre != i)
                    System.out.print(i + " ");
                num = num / i;
                pre = i;
            }
        }

        if (num > 2) {
            if (pre != num)
                System.out.print(num + " ");
            pre = num;
        }
    }

    public static void main(String[] args)
    {
        // Main function
        // Get user's number
        // Calculate result
        // Print result

        System.out.println("-- Prime Factorization -- ");

        inputLimit();
    }
}

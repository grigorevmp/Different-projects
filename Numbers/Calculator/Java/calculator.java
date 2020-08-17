import java.util.Scanner;

public class calculator {

    public static void inputLimit()
    {
        // <input> -> nums and operator
        System.out.println("Type the first number: ");

        Scanner scanner = new Scanner(System.in);
        final int num1 = Integer.parseInt(scanner.nextLine());

        System.out.println("Type the second number: ");
        final int num2 = Integer.parseInt(scanner.nextLine());

        System.out.println("What kind of operation would you like to do? \nChoose between + , -, *, / , ^ : ");
        String op = scanner.nextLine();

        System.out.println(calc(num1, num2, op));

        System.out.println("\nEnter 'y' to continue: ");
        String answer = scanner.nextLine();

        if(answer.toLowerCase().equals("y"))
            inputLimit();
    }

    private static String calc(int num1, int num2, String op) {
        //  N -> fibonacci series
        String a = num1 + " ";
        String b = num2 + " = ";
        String symbols = "+-/*^";

        if(symbols.toLowerCase().contains(op.toLowerCase())){
            switch (op) {
                case "+":
                    return a + op + ' ' + b + (num1 + num2);
                case "-":
                    return a + op + ' ' + b + (num1 - num2);
                case "*":
                    return a + op + ' ' + b + (num1 * num2);
                case "/":
                    return a + op + ' ' + b + (num1 / num2);
                case "^":
                    return a + op + ' ' + b + (Math.pow(num1, num2));

            }
        }
        else
            return "Please only type one of these characters: +, -, *, /!";

        return "";
    }

    public static void main(String[] args)
    {
        // Main function
        // Get user's number
        // Calculate result
        // Print result

        System.out.println("-- Calculator -- ");

        inputLimit();
    }
}

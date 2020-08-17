import java.math.*;
import java.util.Scanner; import java.lang.*;

public class pi {

    public static BigDecimal pi =  BigDecimal.ZERO;
    public static BigDecimal denom1 =  BigDecimal.ONE;
    public static BigDecimal denom2 =  BigDecimal.ONE;
    public static BigDecimal term1 =  BigDecimal.ZERO;
    public static BigDecimal term2 =  BigDecimal.ZERO;

    public static void pi(int x)
    {
        // Nilakantha Series
        // pi = (3 + ((4/(i*(i+1)*(i+2))-(4/((i+2)*(i+3)*(i+4))))))...
        // calculate denominators, terms, then pi

        for(int i=2;i<1000;i+=4)
        {
            denom1 =  BigDecimal.ONE;
            denom1 = denom1.multiply(new BigDecimal(i));
            denom1 = denom1.multiply(new BigDecimal(i+1));
            denom1 = denom1.multiply(new BigDecimal(i+2));

            denom2 =  BigDecimal.ONE;
            denom2 = denom2.multiply(new BigDecimal(i+2));
            denom2 = denom2.multiply(new BigDecimal(i+3));
            denom2 = denom2.multiply(new BigDecimal(i+4));

            term1 = new BigDecimal("4").divide(denom1, 1000, RoundingMode.HALF_UP);
            term2 = new BigDecimal("-4").divide(denom2, 1000, RoundingMode.HALF_UP);

            pi = pi.add(term1);
            pi = pi.add(term2);
        }

        pi = pi.add(new BigDecimal (3));

        pi = pi.setScale(x,  BigDecimal.ROUND_HALF_UP);
    }

    public static void inputLimit()
    {
        // <input> -> digit
        System.out.println("Enter the number of decimals to calculate to: ");

        Scanner scanner = new Scanner(System.in);
        final int digit = Integer.parseInt(scanner.nextLine());

        pi(digit);
        System.out.println("Pi: " + pi);

        pi =  BigDecimal.ZERO;

        System.out.println("Enter '1' to continue: ");
        final int answer = Integer.parseInt(scanner.nextLine());

        if(answer == 1)
            inputLimit();
    }

    public static void main(String[] args)
    {
        // Main function
        System.out.println("-- Find Pi up to the Nth digit --\n");

        inputLimit();
    }
}
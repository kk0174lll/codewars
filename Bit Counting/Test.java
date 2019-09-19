

/**
 * Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
 * <p>
 * Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
 */
public class Test
{

  public static int countBits(int n)
  {
    int BASE = 2;
    int count = 0;
    int d;
    while (n >= BASE) {
      d = n % BASE;
      n = n / BASE;
      count += d;
    }
    count += n;
    return count;
  }

  public static void main(String[] args)
  {
    System.out.println(Integer.toString(424, 2));
    System.out.println(Integer.bitCount(424));
    System.out.println(countBits(424));
  }


}
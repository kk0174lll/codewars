import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

/**
 * Buddy pairs
 * You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.
 * <p>
 * Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:
 * <p>
 * (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1
 * <p>
 * For example 48 & 75 is such a pair:
 * <p>
 * Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
 * Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
 * Task
 * Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n
 * <p>
 * If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil
 * <p>
 * Examples
 * (depending on the languages)
 * <p>
 * buddy(10, 50) returns [48, 75]
 * buddy(48, 50) returns [48, 75]
 * or
 * buddy(10, 50) returns "(48 75)"
 * buddy(48, 50) returns "(48 75)"
 */
class Test
{

  public static String buddy(long start, long limit)
  {
    long n = start;
    long m = start;
    long divN;
    boolean flag = true;
    while (flag && n < limit) {
      divN = divSum(n, Long.MAX_VALUE);
      if ((divN - 1) <= n) {
        n++;
        continue;
      }
      if (n + 1 == divSum(divN - 1, n + 1)) {
        flag = false;
        m = divN - 1;
      } else {
        n++;
      }
    }
    if (!flag) {
      return String.format("(%d %d)", n, m);
    } else {
      return "Nothing";
    }
  }

  public static long divSum(long number, long number2)
  {
    if (number == 0) {
      return 0;
    }
    if (number == 1) {
      return 1;
    }
    long div = 1;
    long lim = (long)Math.sqrt(number);
    for (long i = 2; i <= lim; i++) {
      if (number % i == 0) {
        div += i + number / i;
      }
      if (div > number2) {
        return 0;
      }
    }
    return div;
  }

  public static void main(String[] args)
  {
    System.out.println(buddy(1, 5284));
  }

}
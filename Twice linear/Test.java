import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

/**
 * Consider a sequence u where u is defined as follows:
 * <p>
 * The number u(0) = 1 is the first one in u.
 * For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
 * There are no other numbers in u.
 * Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
 * <p>
 * 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
 * <p>
 * Task:
 * Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
 * <p>
 * Example:
 * dbl_linear(10) should return 22
 */
class Test
{

  public static int dblLinear(int n)
  {
    int[] array = new int[9000000];
    array[1] = 1;
    int x, y, z;
    int j = 0;
    for (int i = 0; i < n; i++) {
      while (j < array.length && array[j] != 1) {
        j++;
      }
      x = j;
      y = 2 * x + 1;
      z = 3 * x + 1;
      array[y] = 1;
      array[z] = 1;
      j++;
    }
    j = 0;
    int i = 0;
    int[] rArray = new int[n + 1];
    while (j < n + 1) {
      if (array[i] == 1) {
        rArray[j] = i;
        j++;
      }
      i++;
    }
    return rArray[n];
  }


  public static void main(String[] args)
  {
    System.out.println(dblLinear(60000));
  }

}
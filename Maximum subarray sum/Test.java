
import java.util.stream.IntStream;

/**
 * The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
 * <p>
 * Max.sequence(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4});
 * // should be 6: {4, -1, 2, 1}
 * Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
 * <p>
 * Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
 */
public class Test
{

  public static int sequence(int[] arr)
  {
    if (arr.length == 0) {
      return 0;
    }
    if (IntStream.of(arr).noneMatch(e -> e > 0)) {
      return 0;
    }
    int max = Integer.MIN_VALUE;
    int currentmax = 0;
    for (int value : arr) {
      currentmax += value;
      if (max < currentmax) {
        max = currentmax;
      }
      if (currentmax < 0) {
        currentmax = 0;
      }
    }
    return max;
  }

  public static void main(String[] args)
  {
    System.out.println(sequence(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4}));

  }


}
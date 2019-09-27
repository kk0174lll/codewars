import java.util.ArrayList;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

import java.util.List;

/**
 * You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
 * <p>
 * 12 ==> 21
 * 513 ==> 531
 * 2017 ==> 2071
 * If no bigger number can be composed using those digits, return -1:
 * <p>
 * 9 ==> -1
 * 111 ==> -1
 * 531 ==> -1
 */
class Test
{

  public static long nextBiggerNumber(long n)
  {
    String strN = String.valueOf(n);
    int size = strN.length();
    int[] arr = Arrays.stream(strN.split("")).mapToInt(Integer::parseInt).toArray();
    if (size == 1) {
      return -1;
    }
    if (size == 2) {
      long newN = n % 10 * 10 + n / 10;
      if (newN > n) {
        return newN;
      } else {
        return -1;
      }
    }
    boolean flag = false;
    int leftValue = 0;
    for (int i = 0; i < size - 1; i++) {
      if (arr[i] < arr[i + 1]) {
        leftValue = i;
        flag = true;
      }
    }
    if (!flag) {
      return -1;
    }
    int temp;
    for (int i = size - 1; i > 0; i--) {
      if (i == leftValue) i--;
      if (arr[i] > arr[leftValue]) {
        temp = arr[i];
        arr[i] = arr[leftValue];
        arr[leftValue] = temp;
        break;
      }
    }
    if (arr[0] == 0) {
      return -1;
    }

    int[] endArray = Arrays.copyOfRange(arr, leftValue + 1, arr.length);
    Arrays.sort(endArray);
    int[] startArray = Arrays.copyOfRange(arr, 0, leftValue + 1);
    long result = 0;
    for (int value : startArray) {
      result = result * 10 + value;
    }
    for (int value : endArray) {
      result = result * 10 + value;
    }
    return result;
  }


  public static void main(String[] args)
  {
    System.out.println(nextBiggerNumber(513));
    //211431603370
    //211431700633L
    //System.out.println(211431700633L);
  }

}
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Write a function stream(int a, int b) -> IntStream that produces the Fibonacci sequence where the first two elements are a and b. Here's the catch: you only get one semicolon!
 */
class Test
{

  public static java.util.stream.IntStream stream(int a, int b) {
    return java.util.stream.Stream.iterate(new int[]{a, b}, i -> new int[]{i[1], i[0] + i[1]}).mapToInt(i -> i[0]);
  }

  public static void main(String[] args)
  {
    System.out.println(Arrays.toString(stream(6, 12).limit(10).toArray()));
  }

}
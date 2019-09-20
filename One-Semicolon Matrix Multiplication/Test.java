/**
 * In this kata, you'll have to write a function multiply(int[][], int[][]) -> int[][] that multiplies two matrices. The matrices are represented by arrays of rows, where each row is an int[]. For example, the 3x3 identity represented this way would be:
 * <p>
 * int[][] ident = new int[][] {
 * new int[] {1, 0, 0},
 * new int[] {0, 1, 0},
 * new int[] {0, 0, 1}
 * };
 * Of course, there's a catch: you only get one semicolon!
 * <p>
 * All the matrices you receive are guaranteed to be valid matrices (i.e. you won't get rows of varying sizes in the same matrix). If a particular multiplication is impossible, your function should return null.
 * <p>
 * For your convenience, a utility function Utils.print(int[][]) -> void has been provided. If you pass it a matrix, it'll print it to the console in a somewhat readable fashion. Remember to remove any debug code in your final answer, though -- can't have any stray semicolons!
 */
class Test
{

  public static int[][] multiply(int[][] a, int[][] b)
  {
    return (a[0].length != b.length) ?
           null :
           java.util.Arrays.stream(a).map(
             i ->
               java.util.stream.IntStream.range(0, b[0].length).map(
                 j ->
                   java.util.stream.IntStream.range(0, b.length).map(x -> i[x] * b[x][j]).sum()
               ).toArray()
           ).toArray(int[][]::new);
  }

  public static void main(String[] args)
  {

    System.out.println(java.util.Arrays.deepToString(multiply(new int[][] {
      new int[] {37, 25},
      new int[] {2, 31},
      new int[] {33, 11},
      new int[] {24, 10},
      }, new int[][] {
      new int[] {33, 28, 18, 20, 42, 39, 38},
      new int[] {10, 4, 7, 14, 48, 44, 28}
    })));
  }

}
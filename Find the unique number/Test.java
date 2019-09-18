import java.util.HashMap;
import java.util.Map;
/*There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance*/
 public class Kata {
    public static double findUniq(double arr[]) {
      Map<Double, Integer> hm = new HashMap<>();
    for(double d : arr){
      hm.compute(d, (k, v) -> (v == null)? 1: v + 1);
    }
    double result = -1;
    for (Map.Entry<Double, Integer> e : hm.entrySet())
    {
      if(e.getValue()==1){
        result = e.getKey();
      }
    }
    return result;
    }
}
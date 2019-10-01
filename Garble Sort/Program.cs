using System;
using System.Linq;

/*Garble Sort
Normally numbers are ordered 1, 2, 3, ..., 9, but in an alternative universe, the numbers are ordered as follows:
7, 9, 6, 4, 1, 3, 5, 8, 2
The task is to create a function called GarbleSort to sort a list of numbers with the values 1 to 9 (inclusive) according to the alternative ordering above.
Examples:
GarbleSort({ 1, 2, 3 }) = { 1, 3, 2 }
GarbleSort({ 5, 6, 3 }) = { 6, 3, 5 }*/
namespace test
{
    class Program
    {
        public static int[] GarbleSort(int[] values)
        {            
            int[] arayPattern = new int[] { 7, 9, 6, 4, 1, 3, 5, 8, 2 };
            int[] resultArray = new int[values.Length];
            int newPosition = 0;
            foreach (int i in arayPattern) {
                foreach (int j in values)
                {
                    if (i == j) {
                        resultArray[newPosition] = j;
                        newPosition++;
                    }
                }
            }
            return resultArray;
            //With Linq
            //return values.Select(x => Array.IndexOf(arayPattern, x)).OrderBy(x => x).Select(x => arayPattern[x]).ToArray();
        }
        static void Main(string[] args)
        {
            
            Console.Out.WriteLine(GarbleSort(new int[] { 1, 2, 3 }));
            Console.ReadKey();
        }
    }
}

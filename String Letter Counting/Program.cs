using System;
using System.Collections.Generic;
using System.Text;


/*Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Ignore all case.

str will never be null.

For Example:

Kata.StringLetterCount("This is a test sentence.") == "1a1c4e1h2i2n4s4t"
Kata.StringLetterCount("") == ""
Kata.StringLetterCount("555") == ""*/
namespace test
{
    class Program
    {

        public static string StringLetterCount(string str)
        {            
            var map = new Dictionary<char, int>();
            char[] alpha = "abcdefghijklmnopqrstuvwxyz".ToCharArray();
            var lowerStr = str.ToLower();
            foreach (var c in lowerStr)
            {
                if (Char.IsLetter(c))
                {
                    if (map.ContainsKey(c))
                    {
                        map[c] = map[c] + 1;
                    }
                    else
                    {
                        map.Add(c, 1);
                    }
                }
            }
            StringBuilder sb = new StringBuilder();
            foreach (var c in alpha)
            {
                if (map.ContainsKey(c))
                {
                    sb.Append(map[c]).Append(c);
                }
            }
            return sb.ToString();
        }


        static void Main(string[] args)
        {
            Console.Out.WriteLine(StringLetterCount("The quick brown fox jumps over the lazy dog."));
            Console.ReadKey();
        }
    }
}

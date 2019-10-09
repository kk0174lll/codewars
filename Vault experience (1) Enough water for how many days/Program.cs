using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

/*Hello dweller,

I'm the overseer of our vault, in which we all live.

I make it short: We are out of water. The only question is when!
Here is a list of all dwellers with their respective age int[] ageOfDweller.
In our tank currently are int water liters of water.
I want to know from you: How long will rich our supplies.

Remember!
Each dweller has a different water consumption.
A dweller under 18 consumes 1 liter per day, everyone older than 50 needs 1.5 liters and the rest needs 2 liters per day.
Each dweller must get its prescribed ration of water, every day!
If not satisfied all dweller, then our days are numbered.

Good luck! I'll bet on you!


Note from Vault Technicians:
Your program returns a positive integer. The residual water is not calculated.
return -1; - If no dweller living inside of the Vault.*/
namespace test
{
    class Program
    {
        public static int ThirstyIn(int water, int[] ageOfDweller)
        {
            double waterPerDay = 0;
            foreach (int age in ageOfDweller)
            {
                if (age < 18)
                {
                    waterPerDay++;
                }
                else
                {
                    if (age > 50)
                    {
                        waterPerDay += 1.5;
                    }
                    else
                    {
                        waterPerDay += 2;
                    }
                }
            }
            return water / (int)waterPerDay;
        }

        static void Main(string[] args)
        {
            Console.Out.WriteLine(ThirstyIn(150, new int[] { 5, 30, 10 }));
            Console.ReadKey();
        }
    }
}

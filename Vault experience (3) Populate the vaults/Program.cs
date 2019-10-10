using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

/*Dear Mr overseer,

we are delighted that they have still managed to us in time.

We have a big problem.

Mankind will be extinct in the near future.
The cause!? - wars, diseases, natural disasters, aliens ... figure it out.
But that’s not the point!

Vault - Tec has started to build vaults around the world. These are huge underground bunkers that allows us to survive.

Your task is to select people and to populate with them these Vaults.
We give you a list of the Vaults and its population capacity public static List<Dweller> PopulateMyVault(int countOfDweller)
We expect you to return a list of the people that you want to put in this vaults. List<Dweller>

However, there are several conditions that must be adhered to:

A male overseer must be uesd in the vault
If more than 50 dweller move in, the overseer must take his "own" wife
with an even number of dweller, number of men and women are equal, who move in
With an odd number of dweller, more women than men needs move in

The mankind bet on you.

Good Luck

Your Vault-Tec Company*/
namespace test
{
    class Program
    {
        public enum Gender
        {
            Mr,
            Mrs
        }
        public enum Position
        {
            overseer,
            none
        }
        public class Dweller
        {
            public Gender Sex { get; set; }

            public Position Work { get; set; }

            public Dweller() : this(Gender.Mr, Position.none) { }

            public Dweller(Gender sex) : this(sex, Position.none) { }

            public Dweller(Gender sex, Position work)
            {
                Sex = sex;
                Work = work;
            }
        }
        public static List<Dweller> PopulateMyVault(int countOfDweller)
        {
            var dwellers = new List<Dweller>();
            if (countOfDweller == 0)
            {
                return dwellers;
            }
            dwellers.Add(new Dweller(Gender.Mr, Position.overseer));
            if (countOfDweller == 1)
            {
                return dwellers;
            }
            int male = 0;
            int female = 0;
            if (countOfDweller % 2 == 0)
            {
                male = countOfDweller / 2;
                female = male;
            }
            else
            {
                male = countOfDweller / 2;
                female = male + 1;
            }
            male--;
            if (countOfDweller > 50)
            {
                dwellers.Add(new Dweller(Gender.Mrs, Position.overseer));
                female--;
            }
            addDvelers(dwellers, male, Gender.Mr);
            addDvelers(dwellers, female, Gender.Mrs);
            return dwellers;
        }
        public static void addDvelers(List<Dweller> dwellers, int count, Gender sex)
        {
            for (int i = 0; i < count; i++)
            {
                dwellers.Add(new Dweller(sex, Position.none));
            }
        }

        static void Main(string[] args)
        {
            Console.Out.WriteLine(PopulateMyVault(10));
            Console.ReadKey();
        }
    }
}

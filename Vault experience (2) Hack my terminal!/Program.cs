using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

/*Ah, you're here! Good.

We have a problem - again.
I've forgot my password of my terminal.
I can only enter my password once again before my terminal is locked and the vault goes down.

All I can give to you is an expression of the current machine code and length of the password that I use.
Find my password in the machine code.
It is the word that have no character on the same place like any other word.

Good luck! I'll bet on you!

Note from the Vault Technicians:

Here is an example of what the Overseer said:

string Code = @"/§TTE§*%RAUM*+?=)PILZ(/&A..-.%BAUM_:";
string Password = "PILZ";
// B A U M
// R A U M
//   ^ ^ ^
// P I L Z

If the Overseer gives you no password length, then the screen saver is active on the terminal.
If he gives you any machine code: the old man sit in front of the coffee machine ...
Your program should
return null;
in these cases.*/
namespace test
{    
    class Program
    {
        public static string HackMyTerminal(int passLength, string machineCode)
        {
            if (passLength == null || passLength == 0) {
                return null;
            }
            string currenWord = "";
            var wordsList = new List<string>();
            foreach (var c in machineCode) {
                if (Char.IsLetter(c))
                {
                    currenWord = currenWord + c;
                    if (currenWord.Length == passLength) {
                        wordsList.Add(currenWord);
                        currenWord = "";
                    }
                }
                else {
                    currenWord = "";
                }
            }
            if (wordsList.Count == 0) {
                return null;
            }
            if (wordsList.Count == 1) {
                return wordsList[0];
            }
            bool flag = false;
            for (int i = 0; i < wordsList.Count; i++) {
                flag = false;
                for (int j = 0; j < wordsList.Count; j++)
                {
                    if (i == j) {
                        continue;
                    }
                    for (int ci = 0; ci < passLength; ci++) {
                        if (wordsList[i][ci] == wordsList[j][ci]) {
                            flag = true;
                            break;
                        }
                    }
                    if (flag) {                        
                        break;
                    }
                }
                if (!flag) {
                    return wordsList[i];
                }
            }            
            return null;
        }

        static void Main(string[] args)
        {            
            Console.Out.WriteLine(HackMyTerminal(8, @"%@|RDR%[()ATZ`-COMPUTER_'&K+RHE]%P)D=@YI$NR'%[X|QPI:C-+VAULTTEC* L, FV = JNJY / MK$#L]OVERSEER(#Z}S/`)@EJ\;+S?QYJ_ZW`;EH=!ATOMPILZ-|KD!*B+J{N}]O[S^APBYY>;-(!*/E`CCFFU"));
            Console.ReadKey();
        }
    }
}

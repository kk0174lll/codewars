using Microsoft.CSharp;
using System;
using System.CodeDom.Compiler;
/*#RunTime Compiler

You have a function Execute to complete.
Three strings are provided for the function.
First string stringToCompile that is C# excutable code like:

using System; public class TextGenerator { public string GetText() { string a = "It is a Test" return a;}}
So the string will be:

"using System; public class TextGenerator { public string GetText() { string a = \"It is a Test\" return a;}}"
The second string className is the class name in stringToCompile:

TextGenerator 
The third string methodName is the function we want to trigate:

GetText
Execute function return an object which is the return of methodName, in example case it is a string: It is a Test*/
namespace test
{
    class Program
    {
        public static object Execute(string stringToCompile, string className, string methodName)
        {
            CSharpCodeProvider provider = new CSharpCodeProvider();
            CompilerParameters parameters = new CompilerParameters();
            parameters.GenerateInMemory = true;            
            CompilerResults results = provider.CompileAssemblyFromSource(parameters, stringToCompile);
            var cls = results.CompiledAssembly.CreateInstance(className);
            var method = cls.GetType().GetMethod(methodName);
            return method.Invoke(cls, null);
        }
        static void Main(string[] args)
        {
            string stringToCompile = "using System; public class TextGenerator { public string Execute() { return \"Hello World\";}}";
            string className = "TextGenerator";
            string methodName = "Execute";
            Console.Out.WriteLine(Execute(stringToCompile, className, methodName));
            Console.ReadKey();
        }
    }
}

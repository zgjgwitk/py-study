using System;
using System.Collections.Generic;
using System.Text;

namespace CallLibrary.Utils
{
    public class CommonHelper
    {
        public string Start(string code)
        {
            Console.Write($"第一个 {code}");
            return code + "CommonHelper";
        }

        public static string StaticMethod()
        {
            Console.Write($"run a special method");
            return "Static";
        }
    }
}

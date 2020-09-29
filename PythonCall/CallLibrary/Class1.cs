using System;

namespace CallLibrary
{
    public class Class1
    {
        public void Start()
        {
            Console.Write("第一个 hello world");
        }
        public void Start(string code)
        {
            Console.Write($"第一个 {code}");
        }
    }
}

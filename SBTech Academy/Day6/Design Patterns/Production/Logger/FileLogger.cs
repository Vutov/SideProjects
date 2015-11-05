namespace Production.Logger
{
    using System;
    using System.IO;

    public class FileLogger : ILogger
    {
        public void Log(string message)
        {
            File.AppendAllLines("../../../log.txt", new[] { message });
            Console.WriteLine("Log to file completed!");
        }
    }
}

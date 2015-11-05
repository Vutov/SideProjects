namespace Print
{
    using System;
    using Connectors;
    using Formatters;
    using Reports;

    public class ProgramMain
    {
        private static void Main(string[] args)
        {
            DIConnector diConnector = new DIConnector();
            IFormatter formatter = diConnector.GetFormatter();

            Report diReport = new DIReport(formatter);
            diReport.Print();

            Console.ReadKey();
        }
    }
}
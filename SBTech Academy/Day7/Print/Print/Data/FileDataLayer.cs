namespace Print.Data
{
    using System;
    using System.IO;

    public class FileDataLayer : DataLayer
    {
        private const string connectionString = "../../../text.txt";

        public override string ConnectionString
        {
            get { return connectionString; }
        }

        public override void GetData()
        {
            string[] file = File.ReadAllLines(this.ConnectionString);
            Console.WriteLine("Data from File:{0}\"{1}\"", Environment.NewLine, string.Join(Environment.NewLine, file));
        }
    }
}

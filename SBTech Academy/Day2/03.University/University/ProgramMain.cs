namespace University
{
    using Interfaces;

    class ProgramMain
    {
        static void Main(string[] args)
        {
            var persons = Faculty.GetPeople();
            foreach (var person in persons)
            {
                var printable = (IPrintable) person;
                printable.PrintName();
                printable.PrintGrade();
            }
        }
    }
}

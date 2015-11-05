namespace University.Person
{
    using System;
    using Interfaces;

    public class Lecturer : IPerson, ILecturer, IPrintable
    {
        public Lecturer(string name, string faculty, string title, double averageGrades)
        {
            this.Name = name;
            this.Faculty = faculty;
            this.Title = title;
            this.AverageGrades = averageGrades;
        }

        public string Name { get; set; }

        public string Faculty { get; set; }

        public string Title { get; set; }

        public double AverageGrades { get; set; }

        public void PrintName()
        {
            Console.WriteLine("Name {0} {1}", this.Title, this.Name);
        }

        public void PrintGrade()
        {
            Console.WriteLine("Grades {0}", this.AverageGrades);
        }
    }
}

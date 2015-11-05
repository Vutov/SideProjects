namespace University.Person
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using Interfaces;

    public class Student : IPerson, IStudent, IPrintable
    {
        public Student(List<double> grades, string name, string faculty)
        {
            this.Grades = grades;
            this.Name = name;
            this.Faculty = faculty;
        }

        public List<double> Grades { get; set; }

        public string Name { get; set; }

        public string Faculty { get; set; }

        public void PrintName()
        {
            Console.WriteLine("Name {0}", this.Name);
        }

        public void PrintGrade()
        {
            Console.WriteLine("Grades {0}", this.Grades.Average());
        }
    }
}

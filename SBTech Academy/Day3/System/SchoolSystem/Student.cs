namespace SchoolSystem
{
    using System.Collections.Generic;

    public class Student
    {
        public Student(int id, string firstName, string lastName, byte age, ICollection<Grade> grades)
        {
            this.Id = id;
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Age = age;
            this.Grades = grades;
        }

        public int Id { get; set; }

        public string FirstName { get; set; }

        public string LastName { get; set; }

        // NB!!! If we use a database, we should NEVER EVER store data, that can be calculated.
        // If we have to create a real student model, we should store it's birth date
        public byte Age { get; set; }

        public ICollection<Grade> Grades { get; set; }
    }
}
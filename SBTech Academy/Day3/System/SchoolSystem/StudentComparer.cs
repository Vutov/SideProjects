namespace SchoolSystem
{
    using System.Collections.Generic;

    public class StudentComparer : IComparer<Student>
    {
        public int Compare(Student x, Student y)
        {
            return x.Age.CompareTo(y.Age);
        }
    }
}

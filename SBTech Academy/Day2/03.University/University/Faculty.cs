namespace University
{
    using System.Collections.Generic;
    using Interfaces;
    using Person;

    public static class Faculty
    {
        public static IEnumerable<IPerson> GetPeople()
        {
            var person = new List<IPerson>
            {
                new Student(new List<double> {2, 3, 4}, "Ivan", "Somewhere"),
                new Student(new List<double> {2, 5, 4, 1}, "Mitko", "Somewhere"),
                new Lecturer("Ivajlo", "Nowhere", "Phd", 3.5)
            };

            return person;
        }
    }
}

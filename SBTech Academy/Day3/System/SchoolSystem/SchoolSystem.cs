namespace SchoolSystem
{
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.Linq;
    using Wintellect.PowerCollections;

    public class SchoolSystem
    {
        private const int NumberOfStudents = 1000;
        private const int NumberOfCourses = 6;
        private static Random rnd;

        private static List<Student> StudentsByName;
        private static IDictionary<int, Student> StudentsById;
        private static OrderedDictionary<int, IList<Student>> StudentsByAge;

        public static void Main()
        {
            StudentsByName = new List<Student>(NumberOfStudents);
            StudentsById = new Dictionary<int, Student>(NumberOfStudents);
            StudentsByAge = new OrderedDictionary<int, IList<Student>>();

            rnd = new Random();

            Stopwatch sw = new Stopwatch();
            Console.Write("Seed time for " + NumberOfStudents + ": ");
            sw.Start();
            //students = GetStudents();
            Seed(NumberOfStudents, NumberOfCourses);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            sw.Restart();
            Console.Write("Get students witch contains letter 'u': ");
            var letter = 'u';
            var studentByLetter = GetStudentByContainingLetter(letter);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by age range with ordered dictionary: ");
            sw.Restart();
            var studentsByAge = GetStudentByAgeRange(20, 22);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by age range with linq dictionary: ");
            sw.Restart();
            var studentsByAgeDict = GetStudentByAgeRangeDict(20, 22);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students sorted by age: ");
            sw.Restart();
            var studentsSortedByAge = GetStudentsByAge();
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by average grade: ");
            sw.Restart();
            var studentsAverageGrade = GetStudentWithAverageGrade();
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students sorted by average grade: ");
            sw.Restart();
            var studentsSortedByGrade = GetStudentSortedByAverageGrade();
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by id 1: ");
            sw.Restart();
            var studentById1 = GetStudentById(1);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by id 358: ");
            sw.Restart();
            var studentById2 = GetStudentById(358);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();

            Console.Write("Get students by id 999: ");
            sw.Restart();
            var studentById3 = GetStudentById(999);
            Console.WriteLine(sw.Elapsed + "\n");
            sw.Stop();
        }

        private static IEnumerable<Student> GetStudentByContainingLetter(char letter)
        {
            var studentsFound = StudentsByName.Where(s => s.FirstName.Contains(letter) || s.LastName.Contains(letter));
            var count = studentsFound.Count();
            return studentsFound;
        }

        private static IEnumerable<StudentView> GetStudentWithAverageGrade()
        {
            var studentsFound = StudentsByName.Select(s => new StudentView()
            {
                Fullname = string.Format("{0} {1}", s.FirstName, s.LastName),
                AverageGrade = s.Grades.Average(g => g.Value)
            });

            return studentsFound;
        }

        private static IEnumerable<StudentView> GetStudentSortedByAverageGrade()
        {
            var studentsFound = StudentsByName.Select(s => new StudentView()
            {
                Fullname = string.Format("{0} {1}", s.FirstName, s.LastName),
                AverageGrade = s.Grades.Average(g => g.Value)
            })
                .OrderBy(s => s.AverageGrade);

            return studentsFound;
        }

        private static Student GetStudentById(int id)
        {
            Student student = null;
            if (StudentsById.ContainsKey(id))
            {
                student = StudentsById[id];
            }
            else
            {
                throw new InvalidOperationException();
            }

            return student;
        }

        private static OrderedDictionary<int, IList<Student>>.View GetStudentByAgeRange(int lower, int upper)
        {
            var students = StudentsByAge.Range(lower, true, upper, true);
            return students;
        }

        private static IEnumerable<KeyValuePair<int, Student>> GetStudentByAgeRangeDict(int lower, int upper)
        {
            var students = StudentsById.Where(s => s.Value.Age >= lower && s.Value.Age <= upper);

            return students;
        }

        private static IEnumerable<Student> GetStudentsByAge()
        {
            StudentsByName.Sort(new StudentComparer());

            return StudentsByName;
        }

        private static void Seed(int numberOfStudents, int numberOfCoures)
        {
            for (int i = 1; i <= numberOfStudents; i++)
            {
                var grades = new List<Grade>(numberOfCoures);
                for (int course = 0; course < numberOfCoures; course++)
                {
                    CourseName name = (CourseName)Enum.ToObject(typeof(CourseName), course);
                    grades.Add(new Grade(name, rnd.Next(2, 7)));
                }

                var student = new Student(i, NameGenerator.GenRandomFirstName(),
                NameGenerator.GenRandomLastName(), (byte)rnd.Next(10, 24), grades);

                StudentsByName.Add(student);
                StudentsById.Add(student.Id, student);
                if (!StudentsByAge.ContainsKey(student.Age))
                {
                    StudentsByAge.Add(student.Age, new List<Student>());
                }

                StudentsByAge[student.Age].Add(student);
            }
        }
    }
}

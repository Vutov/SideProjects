namespace SchoolSystem
{
    public class Grade
    {
        public CourseName Name { get; set; }

        public double Value { get; set; }

        public Grade(CourseName name, double value)
        {
            this.Name = name;
            this.Value = value;
        }
    }
}
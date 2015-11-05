namespace Print.Reports
{
    using Formatters;

    public class DIReport : LetterReport
    {
        public DIReport(IFormatter formatter)
        {
            this.Formatter = formatter;
        }

        protected override void FormatReport()
        {
            this.Formatter.Format();
        }
    }
}

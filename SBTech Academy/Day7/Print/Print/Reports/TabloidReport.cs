namespace Print.Reports
{
    using System;
    using Formatters;

    public class TabloidReport : LetterReport
    {
        protected override void RenderReport()
        {
            Console.WriteLine("Print to tabloid printer");
        }

        protected override void FormatReport()
        {
            this.reportFormatter = new TabloidReportFormatter();
            this.reportFormatter.Format();
        }
    }
}
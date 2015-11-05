namespace Print.Reports
{
    using System;
    using Data;
    using Formatters;

    /// <summary>
    /// This is actually a letter report, but due to yagni, better leave it
    /// like this for now.
    /// </summary>
    public class LetterReport : Report
    {
        private DataLayer dataLayer;

        protected override void RenderReport()
        {
            Console.WriteLine("Print to laser");
        }

        protected override void FormatReport()
        {
            this.reportFormatter = new LetterReportFormatter();
            base.FormatReport();
        }

        protected override void GetData()
        {
            this.dataLayer = new FileDataLayer();
            this.dataLayer.GetData();
        }
    }
}
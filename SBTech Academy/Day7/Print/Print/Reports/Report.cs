namespace Print.Reports
{
    using Formatters;

    public abstract class Report : IPrinter
    {
        protected Formatter reportFormatter;

        public IFormatter Formatter { get; set; }

        public void Print()
        {
            this.GetData();
            this.FormatReport();
            this.RenderReport();
        }

        protected abstract void RenderReport();

        protected virtual void FormatReport()
        {
            this.reportFormatter.Format();
        }

        protected abstract void GetData();
    }
}

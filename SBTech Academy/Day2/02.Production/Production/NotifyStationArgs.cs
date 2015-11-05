namespace Production
{
    public class NotifyStationArgs
    {
        public NotifyStationArgs(string status)
        {
            this.Status = status;
        }

        public string Status { get; set; }
    }
}
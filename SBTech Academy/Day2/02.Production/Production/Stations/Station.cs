namespace Production.Stations
{
    using System;
    using System.Threading;

    public abstract class Station
    {
        public event PropertyChangedEventHandler StationStatusChange;

        public void DoWork()
        {
            var rng = new Random();
            var sleepTime = rng.Next(1, 6);
            Thread.Sleep(sleepTime);
            var message = string.Format("{0} Done", this.GetType().Name);
            this.ChangeStatus(message);
        }

        public abstract Station GetNextPart();

        public delegate void PropertyChangedEventHandler(object sender, NotifyStationArgs eventArgs);

        protected void ChangeStatus(string status)
        {
            var handler = this.StationStatusChange;
            if (handler != null)
            {
                handler(this, new NotifyStationArgs(status));
            }
        }
    }
}

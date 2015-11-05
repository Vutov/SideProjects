namespace Production.Stations
{
    public class Engine : Station
    {
        public override Station GetNextPart()
        {
            return new Seats();
        }
    }
}

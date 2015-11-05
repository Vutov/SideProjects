namespace Production.Stations
{
    public class Seats: Station
    {
        public override Station GetNextPart()
        {
            return new Doors();
        }
    }
}
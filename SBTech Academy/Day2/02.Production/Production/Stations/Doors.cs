namespace Production.Stations
{
    [Logable]
    public class Doors : Station
    {
        public override Station GetNextPart()
        {
            return new Windows();
        }
    }
}

namespace Production.Stations
{
    [Logable]
    public class Wheels : Station
    {
        public override Station GetNextPart()
        {
            return null;
        }
    }
}

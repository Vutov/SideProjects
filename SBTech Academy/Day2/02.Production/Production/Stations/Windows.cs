namespace Production.Stations
{
    public class Windows : Station
    {
        public override Station GetNextPart()
        {
            return new Wheels();
        }
    }
}

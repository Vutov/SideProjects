namespace Production.Stations
{
    using System;

    [Logable]
    public class Chassis : Station
    {
        public override Station GetNextPart()
        {
            return new Body();
        }
    }
}

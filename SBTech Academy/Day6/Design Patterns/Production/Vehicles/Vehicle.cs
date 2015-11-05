namespace Production.Vehicles
{
    using Enum;
    using Interfaces;

    public abstract class Vehicle : IPrintable
    {
        public int Wheels { get; set; }

        public ChassiType Chassis { get; set; }

        public bool Trailer { get; set; }

        public int Doors { get; set; }

        public EngineType Engine { get; set; }

        public BodyType Body { get; set; }

        public int Windows { get; set; }

        public abstract string Print();
    }
}

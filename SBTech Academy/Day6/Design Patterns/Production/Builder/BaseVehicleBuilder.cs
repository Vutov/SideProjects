namespace Production.Builder
{
    using Enum;
    using Logger;
    using Vehicles;

    public abstract class BaseVehicleBuilder
    {
        protected ILogger Logger;

        protected BaseVehicleBuilder(ILogger logger)
        {
            this.Logger = logger;
        }

        public abstract Vehicle Build();

        public int Wheels { get; set; }

        public ChassiType Chassis { get; set; }

        public bool Trailer { get; set; }

        public int Doors { get; set; }

        public EngineType Engine { get; set; }

        public BodyType Body { get; set; }

        public int Windows { get; set; }
    }
}

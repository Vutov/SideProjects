namespace Production.Builder
{
    using Enum;
    using Logger;
    using Vehicles;

    public class TruckBuilder : BaseVehicleBuilder
    {
        public TruckBuilder(ILogger logger)
            : base(logger)
        {
        }

        public override Vehicle Build()
        {
            var truck = new TruckVehicle();
            truck.Engine = base.Engine;
            truck.Body = BodyType.Truck;
            truck.Chassis = base.Chassis;
            truck.Trailer = base.Trailer;
            truck.Doors = base.Doors;
            truck.Wheels = base.Wheels;
            this.Logger.Log(string.Format("Truck completed {0}", truck.Print()));

            return truck;
        }
    }
}

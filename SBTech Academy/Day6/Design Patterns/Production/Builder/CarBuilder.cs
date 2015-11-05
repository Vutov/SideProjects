namespace Production.Builder
{
    using Enum;
    using Logger;
    using Vehicles;

    public class CarBuilder : BaseVehicleBuilder
    {
        public CarBuilder(ILogger logger)
            : base(logger)
        {
        }

        public override Vehicle Build()
        {
            var car = new CarVehicle();
            car.Chassis = base.Chassis;
            car.Body = BodyType.Car;
            car.Engine = base.Engine;
            car.Doors = base.Doors;
            car.Windows = base.Windows;
            car.Wheels = base.Wheels;

            Logger.Log(string.Format("Car completed {0}", car.Print()));
            return car;
        }
    }
}

namespace Production.Fasade
{
    using Builder;
    using Enum;
    using Logger;
    using Vehicles;

    public class VehicleFasade
    {
        private static VehicleFasade instance = null;

        private VehicleFasade()
        {
        }

        public static VehicleFasade Instance
        {
            get
            {
                if (instance == null)
                {
                    instance = new VehicleFasade();
                }

                return instance;
            }
        }

        public TruckVehicle BuildTruck(int wheels, ChassiType chassis, bool trailer, int doors, EngineType engine)
        {
            var logger = new ConsoleLogger();
            BaseVehicleBuilder builder = new TruckBuilder(logger);
            builder.Wheels = wheels;
            builder.Chassis = chassis;
            builder.Trailer = trailer;
            builder.Doors = doors;
            builder.Engine = engine;

            return (TruckVehicle)builder.Build();
        }

        public CarVehicle BuildCar(int wheels, ChassiType chassis, int doors, EngineType engine, int window)
        {
            var logger = new FileLogger();
            BaseVehicleBuilder builder = new CarBuilder(logger);
            builder.Wheels = wheels;
            builder.Chassis = chassis;
            builder.Doors = doors;
            builder.Engine = engine;
            builder.Windows = window;

            return (CarVehicle)builder.Build();
        }
    }
}

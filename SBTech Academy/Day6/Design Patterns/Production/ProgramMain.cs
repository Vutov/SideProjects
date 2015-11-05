namespace Production
{
    using Enum;
    using Fasade;

    public class ProgramMain
    {
        public static void Main(string[] args)
        {
            var fasade = VehicleFasade.Instance;
            fasade.BuildCar(4, ChassiType.TypeA, 4, EngineType.Diesel, 2);
            fasade.BuildTruck(8, ChassiType.TypeB, true, 3, EngineType.Gasoline);
        }
    }
}
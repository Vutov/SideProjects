namespace Production.Vehicles
{
    public class TruckVehicle: Vehicle
    {
        public override string Print()
        {
            return string.Format("doors {1}, trailer {2}, wheels {3}", this.GetType().Name, this.Doors,
                this.Trailer, this.Wheels);
        }
    }
}

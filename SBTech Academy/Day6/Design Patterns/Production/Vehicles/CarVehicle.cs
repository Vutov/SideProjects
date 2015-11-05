namespace Production.Vehicles
{
    public class CarVehicle : Vehicle
    {
        public override string Print()
        {
            return string.Format("doors {1}, windows {2}, wheels {3}", this.GetType().Name, this.Doors,
                this.Windows, this.Wheels);
        }
    }
}

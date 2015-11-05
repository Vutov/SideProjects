namespace Print.Data
{
    public abstract class DataLayer : IDataLayer
    {
        public abstract string ConnectionString { get; }

        public abstract void GetData();
    }
}
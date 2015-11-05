namespace Print.ThirdPartyInterfaces
{
    public interface IFileData : IFileGet, IFileSet
    {
        IConnection Connection { get; set; }
    }
}

namespace Print.Connectors
{
    using System;
    using Formatters;
    using Properties;

    public class DIConnector
    {
        public IFormatter GetFormatter()
        {
            var formatterName = Settings.Default.ReportFormatter;
            var prefixNameSpace = Settings.Default.NameSpace;
            Type type = Type.GetType(prefixNameSpace + "." + formatterName, true);
            return (IFormatter)Activator.CreateInstance(type);
        }
    }
}
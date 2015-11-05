namespace Production
{
    using System;
    using Stations;

    public class ProductionLine
    {
        private ProductionLine line = null;

        private ProductionLine()
        {
        }

        public ProductionLine Line
        {
            get
            {
                if (this.line == null)
                {
                    this.line = new ProductionLine();
                }

                return this.line;
            }
        }

        public static void Start()
        {
            Station nextPart = new Chassis();
            while (nextPart != null)
            {
                foreach (var attribute in nextPart.GetType().CustomAttributes)
                {
                    if (attribute.ToString().Contains("Logable"))
                    {
                        Console.WriteLine("{0} is Loggable!", nextPart.GetType().Name);
                    }
                }

                nextPart.StationStatusChange += (sender, eventArgs) =>
                {
                    Console.WriteLine(eventArgs.Status);
                };

                nextPart.DoWork();

                nextPart = nextPart.GetNextPart();
            }


            //var parts = new List<Station>
            //{
            //    new Chassis(),
            //    new Body(),
            //    new Engine(),
            //    new Seats(),
            //    new Doors(),
            //    new Windows(),
            //    new Wheels()
            //};

            //foreach (var part in parts)
            //{
            //    foreach (var attribute in part.GetType().CustomAttributes)
            //    {
            //        if (attribute.ToString().Contains("Logable"))
            //        {
            //            Console.WriteLine("{0} is Loggable!", part.GetType().Name);
            //        }
            //    }

            //    part.StationStatusChange += (sender, eventArgs) =>
            //    {
            //        Console.WriteLine(eventArgs.Status);
            //    };

            //    part.DoWork();
            //}
        }
    }
}
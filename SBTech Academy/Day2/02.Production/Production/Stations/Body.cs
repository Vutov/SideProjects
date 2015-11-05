using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Production.Stations
{
    [Logable]
    public class Body: Station
    {
        public override Station GetNextPart()
        {
            return new Engine();
        }
    }
}

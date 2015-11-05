using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Data.Repositories
{
    using Models;

    class CustomerRepository: IRepository
    {
        public Customer GetCustomer(string name)
        {
            return null;
        }

        public Customer CreateUser(params string[] param)
        {
            // Validate if something wring throw exception
            return null;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bussiness
{
    using Models;

    public class OrderBuilder
    {
        public ICollection<Item> Items { get; private set; }

        public OrderBuilder(ICollection<Item> items)
        {
            this.Items = items;
        }

        ////For each item ordered,
        ////Validate the entered information.
        ////If not valid, notify the user.
        ////If valid,
        public Order BuildOrder()
        {
            if (this.IsValidCheckout())
            {
                // create order with items init;

                return new Order();
            }

            // return orders for reworking the order from frontend
            return null;
        }

        private bool IsValidCheckout()
        {
            foreach (var item in this.Items)
            {
                if (!ValidateItem(item))
                {
                    return false;
                }
            }

            return true;
        }

        private bool ValidateItem(Item item)
        {
            // Process item and validates it

            return false;
        }
    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DefensiveCodingInitial
{
    using Bussiness;
    using Data;

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var customerValidator = new CustomerValidator();
            customerValidator.ProcessCustomer();

            var orderValidator = new OrderValidator();
            orderValidator.ProcessOrder();

            // Create inventory -> give it the orders, call the inventory
            //// -- Order the items from inventory -- 
            ////For each item ordered,
            ////Locate the item in inventory.
            ////If no longer available, notify the user.
            ////If any items are back ordered and
            ////the customer does not want split orders,
            ////notify the user.
            ////If the item is available,
            ////Decrement the quantity remaining.
            ////Open a connection
            ////Set stored procedure parameters with the inventory data.
            ////Call the save stored procedure.

            // Process the payment with validator, and if everything is all right call the email.
            //// -- Process the payment --
            ////If credit card,
            ////process the credit card payment.
            ////If PayPal,
            ////process the PayPal payment.
            ////If there is a payment problem, notify the user.
            ////Open a connection
            ////Set stored procedure parameters with the payment data.
            ////Call the save stored procedure.

            //// -- Send an email receipt --
            ////If the user requested a receipt
            ////Get the customer data
            ////Ensure a valid email address was provided.
            ////If not,
            ////request an email address from the user.
            ////Open a connection
            ////Set stored procedure parameters with the customer data.
            ////Call the save stored procedure.
            ////If a valid email address is provided,
            ////Send an email.
        }
    }
}

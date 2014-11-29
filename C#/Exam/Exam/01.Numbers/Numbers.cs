using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Numbers
{
    static void Main(string[] args)
    {
        List<int> randomNumbers = new List<int>();
        Random rng = new Random();
        for (int i = 0; i < 15; i++)
        {
            randomNumbers.Add(rng.Next(-150, 250));
        }
        Console.WriteLine("Enter number: ");
        int number = int.Parse(Console.ReadLine());
        Console.WriteLine("Numbers in the list:");
        bool found = false;
        foreach (int num in randomNumbers)
        {
            Console.Write(num + " ");
            if (number == num)
            {
                found = true;
            }
        }
        Console.WriteLine();
        if (found)
        {
            Console.WriteLine("{0} is part of the list.", number);
        }
        else
        {
            Console.WriteLine("{0} is NOT part of the list.", number);
        }

    }
}

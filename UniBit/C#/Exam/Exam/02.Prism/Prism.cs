using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Prism
{
    private double a;
    private double b;
    private double h;

    public Prism(double a, double b, double h)
    {
        this.a = a;
        this.b = b;
        this.h = h;
    }

    public void Show()
    {
        Console.WriteLine("Side one is {0}\nSide two is {1}\nh is {2}", a, b, h);
    }

    public void Volume()
    {
        double v = a * b * h;
        Console.WriteLine("Volume of the prism is {0}", v);
    }

    public void Surface()
    {
        double v = 2 * (a * b + a * h + b * h);
        Console.WriteLine("Surface of the prism is {0}", v);
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Please enter side a: ");
        double a = double.Parse(Console.ReadLine());
        Console.WriteLine("Please enter side b: ");
        double b = double.Parse(Console.ReadLine());
        Console.WriteLine("Please enter side h: ");
        double h = double.Parse(Console.ReadLine());
        Prism myPrism = new Prism(a, b, h);

        myPrism.Show();
        myPrism.Volume();
        myPrism.Surface();

    }
}
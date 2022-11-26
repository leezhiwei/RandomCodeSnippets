using MyShapeApp;

Circle circle1 = new Circle(5.0);
Cylinder cylinder1 = new Cylinder(10.0, 5.0);

void Menu()
{
    Console.WriteLine("---------------- M E N U -----------------");
    Console.WriteLine("[1] Change the radius of circle");
    Console.WriteLine("[2] Change the radius of cylinder");
    Console.WriteLine("[3] Change the length of cylinder");
    Console.WriteLine("[4] Display the area of circle");
    Console.WriteLine("[5] Display the surface area of cylinder");
    Console.WriteLine("[6] Display the volume of cylinder");
    Console.WriteLine("[0] Exit");
    Console.WriteLine("------------------------------------------");
}
while (true)
{
    Menu();
    Console.Write("What is your option: ");
    int input = Convert.ToInt32(Console.ReadLine());
    if (input == 1)
    {
        Console.WriteLine($"Current radius for circle is {circle1.Radius}");
        Console.Write("What do you want to change it to: ");
        double newrad = Convert.ToDouble(Console.ReadLine());
        circle1.Radius = newrad;
    }
    else if (input == 2)
    {
        Console.WriteLine($"Current radius for cylinder is {cylinder1.Radius}");
        Console.Write("What do you want to change it to: ");
        double newrad = Convert.ToDouble(Console.ReadLine());
        cylinder1.Radius = newrad;
    }
    else if (input == 3)
    {
        Console.WriteLine($"Current length for cylinder is {cylinder1.Length}");
        Console.Write("What do you want to change it to: ");
        double newlen = Convert.ToDouble(Console.ReadLine());
        cylinder1.Length = newlen;
    }
    else if (input == 4)
    {
        Console.WriteLine($"Area of circle is {circle1.CalculateArea():F2}");
    }
    else if (input == 5)
    {
        Console.WriteLine($"Surface area of cylinder is {cylinder1.CalculateArea():F2}");
    }
    else if (input == 6)
    {
        Console.WriteLine($"Volume of cylinder is {cylinder1.CalculateVolume():F2}");
    }
    else if (input == 0)
    {
        break;
    }
    else
    {
        Console.WriteLine("Invalid input");
        continue;
    }
}
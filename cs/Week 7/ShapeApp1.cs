
using ShapeApp;
using System.Collections.Generic;
using System.Drawing;

// Create a list to stor Shape objects
List<Circle> circleList = new List<Circle>();  // Q2a


// Q2c  
InitCircleList(circleList);


// Q2d
while (true)
{
    DisplayMenu();
    Console.Write("Enter a option: ");
    string? op = Console.ReadLine(); // put a ? in case not able to read
    if (op == "1")
    {
        Option1(circleList);
        continue;
    }
    else if (op == "2")
    {
        Option2(circleList);
        continue;
    }
    else if (op == "3")
    {
        Option3(circleList);
        continue;
    }
    else if (op == "4")
    {
        Option4(circleList);
        continue;
    }
    else if (op == "5")
    {
        Option5(circleList);
        continue;
    }
    else if (op == "6")
    {
        Option6(circleList);
        continue;
    }
    else if (op == "7")
    {
        Option7(circleList);
        continue;
    }
    else if (op == "0")
    {
        break;
    }
    else
    {
        Console.WriteLine("Invalid option.");
        continue;
    }
}

void Option1(List<Circle> circleList)
{

    int count = 1;
    foreach (Circle c in circleList)
    {
        Console.WriteLine($"[{count}] Type: {c.Type}   Color: {c.Color}  Radius: {c.Radius}");
        count++;
    }
}

void Option2(List<Circle> circleList)
{
    foreach (Circle c in circleList)
    {
        Console.WriteLine(c.ToString() + " " + "Area: " + c.FindArea().ToString("0.00"));
        c.FindArea().ToString("F2");
    }
}

void Option3(List<Circle> circleList)
{
    foreach (Circle n in circleList)
    {
        Console.WriteLine(n.ToString() + "Perimeter: " + n.FindPerimeter().ToString("0.00"));
    }
}

void Option4(List<Circle> circleList)
{
    Option1(circleList); // don't repeat the codes in Option1
    Console.Write("Enter circle number: ");
    int cnn = Convert.ToInt32(Console.ReadLine()); // user enters 1, 2, or 3
    Circle c = circleList[cnn - 1];  // get the correct circle for you.  Don't need a loop.
                                     // then ask for new radius
                                     // and update the radius for this circle.
    Console.Write("Enter new radius: ");
    double nRds = Convert.ToDouble(Console.ReadLine());
    c.Radius = nRds;
    Console.WriteLine("Radius successfully changed.");
}
void Option5(List<Circle> circleList)
{
    Console.Write("Circle color: ");
    string color = Console.ReadLine();
    Console.Write("Circle radius: ");
    double radius = Convert.ToDouble(Console.ReadLine());
    Circle new_circle = new Circle(color, radius);  // must create a new Circle object
    circleList.Add(new_circle);
    Console.WriteLine("New " + new_circle.Color + "circle with radius {0}cm added", radius.ToString());
}
void Option6(List<Circle> circleList)
{
    Option1(circleList);
    Console.Write("Enter circle number: ");
    int index = Convert.ToInt32(Console.ReadLine()) - 1;
    circleList.Remove(circleList[index]);
    Console.WriteLine("Circle removed.");
}
void Option7(List<Circle> circleList)
{
    /*List<Circle> arranged = new List<Circle>();
    double smallestrad = 0;
    foreach (Circle circle in circleList)
    {
        if (circleList.IndexOf(circle) == 0)
        {
            smallestrad = circle.Radius;
            arranged.Add(circle);
        }
        else
        {
            if (circle.Radius < smallestrad)
            {
                smallestrad = circle.Radius;
                Circle c = arranged[0];
                arranged[0] = circle;
                arranged.Add(c);
            }
            else
            {
                arranged.Add(circle);
            }
        }
    }*/
    circleList.Sort();
    foreach (Circle c in circleList)
    {
        Console.WriteLine($"Type: {c.Type} Color: {c.Color} Radius: {c.Radius} Area: {c.FindArea():F2}");

    }
}
void DisplayMenu()
{
    Console.WriteLine("---------------- M E N U --------------------");
    Console.WriteLine("[1] List all the circles\r\n[2] Display the areas of the circles\r\n[3] Display the perimeters of the circles\r\n[4] Change the size of a circle\r\n[5] Add a new circle\r\n[6] Delete a circle\r\n[7] Display circles sorted by area\r\n[0] Exit");
    Console.WriteLine("---------------------------------------------");
}
void InitCircleList(List<Circle> cList)
{
    Circle circle1 = new Circle("Red", 20.0);
    Circle circle2 = new Circle("Green", 10.0);
    Circle circle3 = new Circle("Blue", 30.0);
    cList.Add(circle1);
    cList.Add(circle2);
    cList.Add(circle3);
}
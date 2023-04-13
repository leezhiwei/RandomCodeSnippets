
using ShapeApp;
using System.Collections.Generic;
using System.Data.SqlTypes;
using System.Diagnostics.Metrics;
using System.Drawing;

// Create a list to stor Shape objects
List<Shape> shapeList = new List<Shape>();  // Q2a


// Q2c  
InitShapeList(shapeList);


// Q2d
while (true)
{
    DisplayMenu();
    Console.Write("Enter a option: ");
    string? op = Console.ReadLine(); // put a ? in case not able to read
    if (op == "1")
    {
        Option1(shapeList);
        continue;
    }
    else if (op == "2")
    {
        Option2(shapeList);
        continue;
    }
    else if (op == "3")
    {
        Option3(shapeList);
        continue;
    }
    else if (op == "4")
    {
        Option4(shapeList);
        continue;
    }
    else if (op == "5")
    {
        Option5(shapeList);
        continue;
    }
    else if (op == "6")
    {
        Option6(shapeList);
        continue;
    }
    else if (op == "7")
    {
        Option7(shapeList);
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

void Option1(List<Shape> shapeList)
{
    if (shapeList.Count() == 0)
    {
        Console.WriteLine("No objects in list.");
        return;
    }
    int count = 1;
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            Circle c = (Circle)s;
            Console.WriteLine($"[{count}] Type: {c.Type}   Color: {c.Color}  Radius: {c.Radius}");
        }
        else
        {
            Square sq = (Square)s;
            Console.WriteLine($"[{count}] Type: {sq.Type}   Color: {sq.Color}  Length: {sq.Length}");
        }
        count++;
    }
}

void Option2(List<Shape> shapeList)
{
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            Circle c = (Circle)s;
            Console.WriteLine(c.ToString() + " " + "Area: " + c.FindArea().ToString("0.00"));
            c.FindArea().ToString("F2");
        }
        else
        {
            Square sq = (Square)s;
            Console.WriteLine(sq.ToString() + " " + "Area: " + sq.FindArea().ToString("0.00"));
            sq.FindArea().ToString("F2");
        }
    }
}

void Option3(List<Shape> shapeList)
{
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            Circle c = (Circle)s;
            Console.WriteLine(c.ToString() + " Perimeter: " + s.FindPerimeter().ToString("0.00"));
        }
        else
        {
            Square sq = (Square)s;
            Console.WriteLine(sq.ToString() + " Perimeter: " + sq.FindPerimeter().ToString("0.00"));
        }
    }
}

void Option4(List<Shape> shapeList)
{
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            Circle c = (Circle)s;
            c.Radius += 5;
        }
        else
        {
            Square sq = (Square)s;
            sq.Length += 5;
        }
    }
    Option1(shapeList); // don't repeat the codes in Option1
}
void Option5(List<Shape> shapeList)
{
    Console.Write("Circle color: ");
    string color = Console.ReadLine();
    Console.Write("Circle radius: ");
    double radius = Convert.ToDouble(Console.ReadLine());
    Circle new_circle = new Circle(color, radius);  // must create a new Circle object
    shapeList.Add(new_circle);
    Console.WriteLine("New " + new_circle.Color + "circle with radius {0}cm added", radius.ToString());
}
void Option6(List<Shape> shapeList)
{
    if (shapeList.Count == 0)
    {
        Console.WriteLine("No objects in list");
        return;
    }
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            break;
        }
        else
        {
            Console.WriteLine("No circle objects");
            return;
        }
    }
    Option1(shapeList);
    Console.Write("Enter circle number: ");
    int index = Convert.ToInt32(Console.ReadLine()) - 1;
    if (shapeList[index] is Circle)
    {
        shapeList.Remove(shapeList[index]);
        Console.WriteLine("Circle removed.");
    }
    else
    {
        Console.WriteLine("Not a circle.");
    }
    
}
void Option7(List<Shape> shapeList)
{
    /*List<Shape> arranged = new List<Shape>();
    double smallestrad = 0;
    foreach (Circle circle in shapeList)
    {
        if (shapeList.IndexOf(circle) == 0)
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
    shapeList.Sort();
    foreach (Shape s in shapeList)
    {
        if (s is Circle)
        {
            Circle c = (Circle)s;
            Console.WriteLine($"Type: {c.Type} Color: {c.Color} Radius: {c.Radius} Area: {c.FindArea():F2}");
        }
        else
        {
            Square sq = (Square)s;
            Console.WriteLine($"Type: {sq.Type} Color: {sq.FindArea()} Radius: {sq.FindArea()} Area: {sq.FindArea():F2}");
        }
    }
}
void DisplayMenu()
{
    Console.WriteLine("---------------- M E N U --------------------");
    Console.WriteLine("[1] List all the shapes\r\n[2] Display the areas of the shapes\r\n[3] Display the perimeters of the shapes\r\n[4] Change the sizes of a shapes\r\n[5] Add a new circle\r\n[6] Delete a circle\r\n[7] Display shapes sorted by area\r\n[0] Exit");
    Console.WriteLine("---------------------------------------------");
}
void InitShapeList(List<Shape> cList)
{
    Circle shape1 = new Circle("Red", 20.0);
    Square shape2 = new Square("Red", 10.0);
    Circle shape3 = new Circle("Green", 10.0);
    Square shape4 = new Square("Green", 20.0);
    Circle shape5 = new Circle("Blue", 30.0);
    Square shape6 = new Square("Blue", 30);
    cList.Add(shape1);
    cList.Add(shape2);
    cList.Add(shape3);
    cList.Add(shape4);
    cList.Add(shape5);
    cList.Add(shape6);
}
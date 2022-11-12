// See https://aka.ms/new-console-template for more information

using PointApp;
// create 2 points
Point p1 = new Point(2, 2);
Point p2 = new Point(5, 5);

// find distance between these 2 points
double dist = p1.Distance(p2);
Console.WriteLine($"The distance between p1({p1.X},{p1.Y}) and p2({p2.X},{p2.Y}) is {dist:F2}");
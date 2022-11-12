// See https://aka.ms/new-console-template for more information
using RectangleProject;
// Create 2 Rectangle objects
Rectangle rect1 = new Rectangle(50, 100);
Rectangle rect2 = new Rectangle(100, 250);

// Display the attributes of rect1
Console.WriteLine($"The attributes of Rectangle 1 are {rect1}");

// Display the area of rect1
Console.WriteLine("The area of rectangle 1 is " + rect1.FindArea());

// Display the perimeter of rect2
Console.WriteLine("The perimeter of rectangle 2 is " + rect2.FindPerimeter()); 
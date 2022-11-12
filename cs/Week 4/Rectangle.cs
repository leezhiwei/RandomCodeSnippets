using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RectangleProject
{
    internal class Rectangle
    {   // attribute
        private double width;

        public double Width  // property, use attribute name 
        {
            get { return width; }  // long version of get and set
            set { width = value; }
        }
        // attribute
        private double height;

        public double Height { get; set; }  // simplified get and set

        public Rectangle()  // default constructor
        {
            width = 1; // must give the attributes some default values
            height = 1;
        }

        public Rectangle(double w, double h)
        { // use different from attribute name 
            width = w;  // do not use property name, use attribute name
            height = h;
        }

        public double FindArea()
        {
            double area = height * width;
            return area;
        }
        public double FindPerimeter()
        {
            double perimeter = height * 2 + width * 2;
            return perimeter;
        }

        public override string ToString()
        {
            return "height: " + Convert.ToString(height)
            + " width: " + Convert.ToString(width);

        }


    }
}

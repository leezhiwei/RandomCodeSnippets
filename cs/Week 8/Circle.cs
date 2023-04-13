namespace ShapeApp
{
    public class Circle : Shape, IComparable<Circle> // inherit abstract class
    {
        // Attributes
        public double Radius { get; set; }

        // Constructors
        public Circle() : base()
        {
            Radius = 1.0;
        }
        public Circle(string c, double r) : base("Circle", c)
        {
            Radius = r;
        }

        // Other methods
        public int CompareTo(Circle c)
        {
            if (Radius > c.Radius)
            {
                return 1;
            }
            else if (Radius == c.Radius)
            {
                return 0;
            }
            else
            {
                return -1;
            }
        }

        // override the abstract method
        public override double FindArea()
        {
            return Math.PI * Radius * Radius;
        }

        // ToString() method
        public override string ToString()
        {
            return base.ToString()
                + "\tRadius: " + Radius;
        }
        public override double FindPerimeter()
        {
            double pi = Math.PI;
            return (pi * (2 * Radius));
        }
    }
}
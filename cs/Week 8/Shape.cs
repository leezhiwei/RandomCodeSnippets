namespace ShapeApp
{
    public abstract class Shape: IComparable<Shape>
    {
        private string type;
        private string color;
        // Attributes
        public string Type { get; set; }
        public string Color { get; set; }

        // Constructors
        public Shape() { }
        public Shape(string type, string col)
        {
            Type = type;
            Color = col;
        }

        // Abstract methods
        public abstract double FindArea();

        // Find FindPerimeter
        public abstract double FindPerimeter();

        // ToString()
        public override string ToString()
        {
            return "Type: " + Type
                + "\tColor: " + Color;
        }
        public int CompareTo(Shape s)
        {
            if (FindArea() > s.FindArea())
            {
                return 1;
            }
            else if (FindArea() == s.FindArea())
            {
                return 0;
            }
            else
            {
                return -1;
            }
        }

    }
}


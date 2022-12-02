namespace ShapeApp
{
    public abstract class Shape
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


    }
}


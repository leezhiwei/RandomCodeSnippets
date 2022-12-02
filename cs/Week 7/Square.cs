namespace ShapeApp
{
    class Square : Shape  // inherit abstract class
    {
        // Attribute
        public double Length { get; set; }

        // Constructor
        public Square() : base()
        {
            Length = 1.0;
        }
        public Square(string c, double len) : base("Square", c)
        {
            Length = len;
        }

        // override the abstract method
        public override double FindArea()
        {
            return Length * Length;
        }
        public override double FindPerimeter()
        {
            return Length * 4;
        }
        public override string ToString()
        {
            return base.ToString() +
                 "\tLength: " + Length;
        }

    }
}
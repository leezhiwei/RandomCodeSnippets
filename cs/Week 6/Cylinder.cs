namespace MyShapeApp
{
    internal class Cylinder : Circle
    {
        private double length;
        public double Length { get; set; }

        public Cylinder() : base()
        {
            Length = 0;
        }
        public Cylinder(double len, double rad) : base(rad)
        {
            Length = len;
        }
        public override double CalculateArea()
        {
            return (2 * Math.PI * Radius * Length) + (2 * Math.PI * (Math.Pow(Radius, 2)));
        }
        public double CalculateVolume()
        {
            return base.CalculateArea() * Length;
        }
        public override string ToString()
        {
            return base.ToString() + " " + $"Length : {Length} Area of Cylinder : {CalculateArea()} Volume of Cylinder : {CalculateVolume()}";
        }
    }
}

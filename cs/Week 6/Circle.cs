namespace MyShapeApp
{
    internal class Circle
    {
        private double radius;
        public double Radius { get; set; }
        public Circle()
        {
            Radius = 0;
        }
        public Circle(double rad)
        {
            Radius = rad;
        }
        public virtual double CalculateArea()
        {
            return Math.PI * (Math.Pow(Radius,2));
        }
        public override string ToString()
        {
            return $"Radius {Radius}, Area Circle {CalculateArea()}";
        }
    }
}

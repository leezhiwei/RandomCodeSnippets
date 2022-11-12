namespace FareCalcClasses
{
    internal class BusStop
    {
        private double distance;
        private string code;
        private string road;
        private string description;

        public BusStop(double dist1, string code1, string road1, string description1)
        {
            distance = dist1;
            code = code1;
            road = road1;
            description = description1;
        }
        public override string ToString()
        {
            return $"{distance}, {code}, {road}, {description}";
        }
    }
    internal class Fare
    {
        private double upToDistance;
        private int amount;

        public Fare(double Dist1, int amount1)
        {
            upToDistance = Dist1;
            amount = amount1;
        }
        public override string ToString()
        {
            return $"{upToDistance}, {amount}";
        }
    }
}

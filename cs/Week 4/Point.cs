using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PointApp
{
    internal class Point
    {
        // attributes
        private int x;
        private int y;

        // properties
        public int X { get; set; }
        public int Y { get; set; }

        // constructors
        public Point()
        {
            x = 0;  // Usually we use 0 (the origin).
            y = 0;
        }
        public Point(int xa, int ya)
        {
            X = xa;
            Y = ya;
        }


        // calculate distance between point p and myself (that has x and y)
        public double Distance(Point p)
        {  // You are using X and x which belongs to this class
           // You should use the x and y that belongs to p in the formula 
            double distance = Math.Sqrt(((p.X - x) ^ 2) + ((p.Y - y) ^ 2));
            return distance;
        }
    }
}

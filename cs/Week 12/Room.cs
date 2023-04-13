using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hospital
{
    internal class Room
    {
        public string Location { get; set; }
        public string WardClass { get; set; }
        public Room() { }
        public Room(string loc, string wc)
        {
            Location = loc;
            WardClass = wc;
        }
        public override string ToString()
        {
            return $"Location: {Location}, WardClass: {WardClass}";
        }
    }
}

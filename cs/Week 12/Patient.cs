using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hospital
{
    internal class Patient:Person
    {
        public Room WardedAt { get; set; }
        public Patient() : base() { }
        public Patient(string nr, string na, Room wa):base(nr,na)
        {
            WardedAt = wa;
        }
        public override string ToString()
        {
            return base.ToString() + $" Warded at {WardedAt.ToString()}";
        }
    }
}

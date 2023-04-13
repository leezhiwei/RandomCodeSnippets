using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hospital
{
    internal class Doctor : Person
    {
        public string Department { get; set; }
        public List<Patient> PatientList { get; set; } = new List<Patient>();
        public Doctor():base() { }
        public Doctor(string nr, string na, string de): base(nr, na)
        {
            Department = de;
        }
        public void AddPatient(Patient p)
        {
            PatientList.Add(p);
        }
        public bool RemovePatient(Patient p)
        {
            bool result = PatientList.Remove(p);
            return result;
        }
        public override string ToString()
        {
            string pinfo = "";
            foreach (Patient p in PatientList)
            {
                pinfo += $"Name: {p.Name}, NRIC: {p.NRIC} ";
            }
            return base.ToString() + $" Department: {Department}" + $" PatientInfo: {pinfo}";
        }
    }
}

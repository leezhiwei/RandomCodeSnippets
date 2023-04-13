using Hospital;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Xml.Serialization;

List<Room> roomList = new List<Room>();
List<Patient> patientList = new List<Patient>();
List<Doctor> doctorList = new List<Doctor>();

void InitData()
{
    roomList.Add(new Room("#01-01", "C"));
    roomList.Add(new Room("#02-02", "B"));
    roomList.Add(new Room("#03-03", "A"));
    roomList.Add(new Room("#04-04", "A"));
    doctorList.Add(new Doctor("S1234567A", "Tom", "Pediatrics"));
    doctorList.Add(new Doctor("S2345678A", "Champ", "Oncology"));
    doctorList.Add(new Doctor("S3456789B", "Terry", "Cardiology"));
}
InitData();
void CreatePatients()
{
    string[] data = File.ReadAllLines("Patients.csv");
    List<List<string>> splitted = new List<List<string>>();
    for (int x = 1; x < data.Length; x++)
    {
        splitted.Add(new List<string>(data[x].Split(',')));
    }
    foreach (List<string> patients in splitted)
    {
        Room patientin = null;
        foreach (Room r in roomList)
        {
            if (r.Location == patients[2])
            {
                patientin = r;
                break;
            }
        }
        patientList.Add(new Patient(patients[0], patients[1], patientin));
    }
}
CreatePatients();
foreach (Patient p in patientList)
{
    Console.WriteLine(p.ToString());
}
int SearchDoctor(string nr, List<Doctor> dlist)
{
    foreach (Doctor d in dlist)
    {
        if (nr == d.NRIC)
        {
            return dlist.IndexOf(d);
        }
    }
    return -1;
}
int SearchPatients(string nr, List<Patient> plist)
{
    foreach (Patient p in plist)
    {
        if (p.NRIC == nr)
        {
            return plist.IndexOf(p);
        }
    }
    return -1;
}
void AssignPatientsToDoctors()
{
    string[] data = File.ReadAllLines("PatientsToDoctor.csv");
    List<List<string>> splitted = new List<List<string>>();
    for (int x = 1; x < data.Length; x++)
    {
        splitted.Add(new List<string>(data[x].Split(',')));
    }
    foreach (List<string> line in splitted)
    {
        int indexd = SearchDoctor(line[2], doctorList);
        int indexp = SearchPatients(line[0], patientList);
        if (indexd == -1 || indexp == -1)
        {
            Console.WriteLine("No patient or doctor found.");
            continue;
        }
        else
        {
            doctorList[indexd].AddPatient(patientList[indexp]);
        }
    }
}
AssignPatientsToDoctors();
foreach (Doctor d in doctorList)
{
    Console.WriteLine(d.ToString());
}
void RemovePatientFromDoctor()
{
    Console.Write("What is the NRIC of the patient you want to remove? ");
    bool result = false;
    string pnric = Console.ReadLine();
    int indexp = SearchPatients(pnric, patientList);
    if (indexp == -1)
    {
        Console.WriteLine("No such patient exists.");
        return;
    }
    foreach (Doctor d in doctorList)
    {
        result = d.RemovePatient(patientList[indexp]);
        if (result)
        {
            break;
        }
    }
    if (!result)
    {
        Console.WriteLine("Patient not assigned to doctor.");
    }
}
RemovePatientFromDoctor();
foreach (Doctor d in doctorList)
{
    Console.WriteLine(d.ToString());
}
void AddNewPatient()
{
    Console.Write("What is the patient's name? ");
    string name = Console.ReadLine();
    Console.Write("What is the patients's NRIC? ");
    string nric = Console.ReadLine();
    Console.Write("What is the location of the patient? ");
    string room = Console.ReadLine();
    Room loc = null;
    foreach (Room r in roomList)
    {
        if (r.Location == room)
        {
            loc = r;
            break;
        }
    }
    if (loc is null)
    {
        Console.WriteLine("Invalid location");
        return;
    }
    Patient newp = new Patient(nric, name, loc);
    patientList.Add(newp);
    string csvfile = @"Patients.csv";
    using(StreamWriter sw = File.AppendText(csvfile))
    {
        sw.WriteLine();
        sw.WriteLine($"{nric}, {name}, {room}");
        sw.Close();
    }
    Console.WriteLine(patientList.Last().ToString());
    string[] data = File.ReadAllLines(csvfile);
    Console.WriteLine(data.Last());
}
AddNewPatient();
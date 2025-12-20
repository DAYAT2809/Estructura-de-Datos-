using System;

namespace RegistroEstudiante
{
    class Estudiante
    {
        public int Id;
        public string Nombres;
        public string Apellidos;
        public string Direccion;
        public string[] Telefonos = new string[3];

        public void MostrarDatos()
        {
            Console.WriteLine("\n--- DATOS DEL ESTUDIANTE ---");
            Console.WriteLine($"ID: {Id}");
            Console.WriteLine($"Nombres: {Nombres}");
            Console.WriteLine($"Apellidos: {Apellidos}");
            Console.WriteLine($"Dirección: {Direccion}");
            Console.WriteLine("Teléfonos:");

            for (int i = 0; i < Telefonos.Length; i++)
            {
                Console.WriteLine($"Teléfono {i + 1}: {Telefonos[i]}");
            }
        }
    }
}

using System;
using System.IO;

class Program
{
    static void Main()
    {
        // Nombre de la carpeta
        string carpeta = "vuelos_baratos";

        // Verificar si la carpeta existe, si no, crearla
        if (!Directory.Exists(carpeta))
        {
            Directory.CreateDirectory(carpeta);
            Console.WriteLine($"Carpeta '{carpeta}' creada con éxito.");
        }
        else
        {
            Console.WriteLine($"La carpeta '{carpeta}' ya existe.");
        }

        // Crear archivo de código (ejemplo: vuelos.txt)
        string archivo = Path.Combine(carpeta, "vuelos.txt");

        if (!File.Exists(archivo))
        {
            File.WriteAllText(archivo, 
@"Quito,Bogotá,120,08:00
Quito,Cartagena,180,12:00
Quito,Cartagena,150,16:00
Bogotá,Cartagena,90,10:00
Bogotá,Quito,120,14:00");
            Console.WriteLine($"Archivo '{archivo}' creado con éxito.");
        }
        else
        {
            Console.WriteLine($"El archivo '{archivo}' ya existe.");
        }
    }
}
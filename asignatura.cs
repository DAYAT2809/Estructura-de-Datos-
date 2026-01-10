using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Lista de asignaturas
        List<string> asignaturas = new List<string>() 
        { 
            "Matemáticas", 
            "Física", 
            "Química", 
            "Historia", 
            "Lengua" 
        };

        // Recorrer la lista e imprimir el mensaje
        foreach (string asignatura in asignaturas)
        {
            Console.WriteLine("Yo estudio " + asignatura);
        }

        // Para que la consola no se cierre inmediatamente
        Console.WriteLine("Presiona cualquier tecla para salir...");
        Console.ReadKey();
    }
}

using System;
using System.Collections.Generic;

class LoteriaPrimitiva
{
    static void Main()
    {
        List<int> numeros = new List<int>();

        Console.WriteLine("Ingrese los números ganadores de la lotería primitiva:");

        // Pedimos 6 números al usuario (puedes ajustar si quieres otro número de números)
        for (int i = 0; i < 6; i++)
        {
            int num;
            bool valido;
            do
            {
                Console.Write($"Número {i + 1}: ");
                valido = int.TryParse(Console.ReadLine(), out num);

                if (!valido || num < 1 || num > 49) // rango típico de la lotería primitiva
                {
                    Console.WriteLine("Número inválido. Debe ser un número entre 1 y 49.");
                    valido = false;
                }
                else if (numeros.Contains(num))
                {
                    Console.WriteLine("Número repetido. Ingrese otro.");
                    valido = false;
                }
            } while (!valido);

            numeros.Add(num);
        }
        
        // Ordenamos la lista
        numeros.Sort();

        // Mostramos los números ordenados
        Console.WriteLine("\nNúmeros ganadores ordenados:");
        foreach (int n in numeros)
        {
            Console.Write(n + " ");
        }

        Console.WriteLine("\n\nPresiona cualquier tecla para salir...");
        Console.ReadKey();
    }
}
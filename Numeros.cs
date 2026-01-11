using System;
using System.Collections.Generic;

class Programa
{
    static void Main()
    {
        // Crear la lista con los números del 1 al 10
        List<int> numeros = new List<int>();
        for (int i = 1; i <= 10; i++)
        {
            numeros.Add(i);
        }

        // Mostrar la lista en orden inverso separada por comas
        for (int i = numeros.Count - 1; i >= 0; i--)
        {
            Console.Write(numeros[i]);
            if (i > 0) // Para no poner la coma al final
                Console.Write(",");
        }

        Console.WriteLine(); // Salto de línea al final
    }
}

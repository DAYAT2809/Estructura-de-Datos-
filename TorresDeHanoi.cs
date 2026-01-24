using System;
using System.Collections.Generic;

class TorresDeHanoi
{
    /// <summary>
    /// Método principal del ejercicio
    /// </summary>
    public static void Ejecutar()
    {
        Console.Write("\nIngrese el número de discos: ");
        int n = int.Parse(Console.ReadLine());

        Stack<int> origen = new Stack<int>();
        Stack<int> auxiliar = new Stack<int>();
        Stack<int> destino = new Stack<int>();

        // Se cargan los discos en la torre origen
        for (int i = n; i >= 1; i--)
         {
            origen.Push(i);
        }

        Console.WriteLine("\nMovimientos de las Torres de Hanoi:\n");
        ResolverHanoi(n, origen, auxiliar, destino,
                      "Origen", "Auxiliar", "Destino");
    }

    /// <summary>
    /// Algoritmo recursivo de Hanoi usando pilas
    /// </summary>
    static void ResolverHanoi(int n,
        Stack<int> origen, Stack<int> aux, Stack<int> dest,
        string nomOri, string nomAux, string nomDest)
    {
        if (n == 1)
        {
            int disco = origen.Pop();
            dest.Push(disco);
            Console.WriteLine($"Mover disco {disco} de {nomOri} a {nomDest}");
            return;
        }

         ResolverHanoi(n - 1, origen, dest, aux, nomOri, nomDest, nomAux);

        int discoActual = origen.Pop();
        dest.Push(discoActual);
        Console.WriteLine($"Mover disco {discoActual} de {nomOri} a {nomDest}");

        ResolverHanoi(n - 1, aux, origen, dest, nomAux, nomOri, nomDest);
    }
}
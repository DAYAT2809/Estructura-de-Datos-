using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        LinkedList<int> lista = new LinkedList<int>();
        Random rnd = new Random();

        // 1. Crear la lista enlazada con 50 números aleatorios
        for (int i = 0; i < 50; i++)
        {
            lista.AddLast(rnd.Next(1, 1000)); // 1 a 999
        }

        Console.WriteLine("Lista original:");
        MostrarLista(lista);

        // 2. Leer rango desde teclado
        Console.Write("\nIngrese el valor mínimo del rango: ");
        int min = int.Parse(Console.ReadLine());

        Console.Write("Ingrese el valor máximo del rango: ");
        int max = int.Parse(Console.ReadLine());

        // 3. Eliminar nodos fuera del rango
        EliminarFueraDeRango(lista, min, max);

        Console.WriteLine("\nLista después de eliminar los nodos fuera del rango:");
        MostrarLista(lista);

        Console.ReadKey();
    }

    static void EliminarFueraDeRango(LinkedList<int> lista, int min, int max)
    {
        var nodo = lista.First;

        while (nodo != null)
        {
            var siguiente = nodo.Next;

            if (nodo.Value < min || nodo.Value > max)
                lista.Remove(nodo);

            nodo = siguiente;
        }
    }

    static void MostrarLista(LinkedList<int> lista)
    {
        foreach (int n in lista)
            Console.Write(n + " ");
        Console.WriteLine();
    }
}

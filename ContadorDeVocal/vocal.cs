using System;

class ProgramaVocales
{
    static void Main()
    {
        // Pedimos al usuario que ingrese una palabra
        Console.Write("Ingrese una palabra: ");
        string palabra = Console.ReadLine().ToLower(); // Convertimos a minúsculas

        // Inicializamos contadores para cada vocal
        int a = 0, e = 0, i = 0, o = 0, u = 0;

        // Recorremos cada letra de la palabra
        foreach (char letra in palabra)
        {
            switch (letra)
            {
                case 'a':
                    a++;
                    break;
                case 'e':
                    e++;
                    break;
                case 'i':
                    i++;
                    break;
                case 'o':
                    o++;
                    break;
                case 'u':
                    u++;
                    break;
            }
        }

        // Mostramos los resultados
        Console.WriteLine("\nCantidad de cada vocal:");
        Console.WriteLine($"a: {a}");
        Console.WriteLine($"e: {e}");
        Console.WriteLine($"i: {i}");
        Console.WriteLine($"o: {o}");
        Console.WriteLine($"u: {u}");
    }
}

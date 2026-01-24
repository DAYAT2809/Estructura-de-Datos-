sing System;
using System.Collections.Generic;

class BalanceoParentesis
{
    /// <summary>
    /// Método principal del ejercicio
    /// </summary>
    public static void Ejecutar()
    {
        Console.Write("\nIngrese la expresión matemática: ");
        string expresion = Console.ReadLine();

        if (EstaBalanceado(expresion))
            Console.WriteLine("Fórmula balanceada.");
        else
            Console.WriteLine("Fórmula NO balanceada.");
    }

    /// <summary>
    /// Verifica si los símbolos están balanceados usando una pila
    /// </summary>
    static bool EstaBalanceado(string expresion)
    {
        Stack<char> pila = new Stack<char>();

        foreach (char c in expresion)
        {
            // Símbolos de apertura
            if (c == '(' || c == '{' || c == '[')
            {
                pila.Push(c);
            }
            // Símbolos de cierre
            else if (c == ')' || c == '}' || c == ']')
             {
                if (pila.Count == 0)
                    return false;

                char tope = pila.Pop();

                if ((c == ')' && tope != '(') ||
                    (c == '}' && tope != '{') ||
                    (c == ']' && tope != '['))
                    return false;
            }
        }

        return pila.Count == 0;
    }
}
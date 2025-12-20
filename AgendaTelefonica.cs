using System;
using System.Collections.Generic;
using System.Linq;

class Contacto
{
    public string Nombre;
    public string Telefono;
    public string Correo;
    public string Direccion;

    public Contacto(string nombre, string telefono, string correo, string direccion)
    {
        Nombre = nombre;
        Telefono = telefono;
        Correo = correo;
        Direccion = direccion;
    }

    public override string ToString()
    {
        return $"Nombre: {Nombre}, Teléfono: {Telefono}, Correo: {Correo}, Dirección: {Direccion}";
    }
}

class Program
{
    static List<Contacto> contactos = new List<Contacto>();

    static void Main()
    {
        // Contactos predefinidos
        contactos.Add(new Contacto("Scarleth Tenecoya", "0991234567", "scarleth@email.com", "Quito"));
        contactos.Add(new Contacto("Dayo Pérez", "0987654321", "dayo@email.com", "Quito"));
        contactos.Add(new Contacto("Ana López", "0991122334", "ana@email.com", "Guayaquil"));

        int opcion;

        do
        {
            Console.WriteLine("\n--- AGENDA TELEFÓNICA ---");
            Console.WriteLine("1. Agregar contacto");
            Console.WriteLine("2. Mostrar todos los contactos");
            Console.WriteLine("3. Buscar contacto");
            Console.WriteLine("4. Eliminar contacto");
            Console.WriteLine("5. Salir");
            Console.Write("Seleccione una opción: ");

            opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    AgregarContacto();
                    break;
                case 2:
                    MostrarTodos();
                    break;
                case 3:
                    BuscarContacto();
                    break;
                case 4:
                    EliminarContacto();
                    break;
                case 5:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }

        } while (opcion != 5);
    }

    static void AgregarContacto()
    {
        Console.Write("Nombre: ");
        string nombre = Console.ReadLine();

        Console.Write("Teléfono: ");
        string telefono = Console.ReadLine();

        Console.Write("Correo: ");
        string correo = Console.ReadLine();

        Console.Write("Dirección: ");
        string direccion = Console.ReadLine();

        contactos.Add(new Contacto(nombre, telefono, correo, direccion));
        Console.WriteLine("Contacto agregado correctamente.");
    }

    static void MostrarTodos()
    {
        Console.WriteLine("\nContactos en la agenda:");

        if (contactos.Count == 0)
        {
            Console.WriteLine("No hay contactos.");
            return;
        }

        foreach (var c in contactos)
        {
            Console.WriteLine(c);
        }
    }

    static void BuscarContacto()
    {
        Console.Write("Ingrese el nombre a buscar: ");
        string nombre = Console.ReadLine();

        var encontrado = contactos
            .FirstOrDefault(c => c.Nombre.ToLower() == nombre.ToLower());

        if (encontrado != null)
        {
            Console.WriteLine("Contacto encontrado: " + encontrado);
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }

    static void EliminarContacto()
    {
        Console.Write("Ingrese el nombre a eliminar: ");
        string nombre = Console.ReadLine();

        var encontrado = contactos
            .FirstOrDefault(c => c.Nombre.ToLower() == nombre.ToLower());

        if (encontrado != null)
        {
            contactos.Remove(encontrado);
            Console.WriteLine("Contacto eliminado.");
        }
        else
        {
            Console.WriteLine("Contacto no encontrado.");
        }
    }
}
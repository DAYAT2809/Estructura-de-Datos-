# Cuentas bancarias

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor: crea cuenta de un titular con saldo inicial.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con saldo inicial de ${self.saldo}")

    def depositar(self, cantidad):
        """
        Depositar una cantidad de dinero en la cuenta.
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de ${cantidad} en la cuenta de {self.titular}. Saldo actual: ${self.saldo}")
        else:
            print("El monto a depositar debe ser un número positivo.")

    def retirar(self, cantidad):
        """
        Retirar una cantidad de dinero de la cuenta si hay saldo suficiente.
        """
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} de la cuenta de {self.titular}. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def __del__(self):
        """
        Destructor: se llama cuando la cuenta se cierra (objeto destruido).
        """
        print(f"Cuenta de {self.titular} cerrada. Saldo final: ${self.saldo}")

# Ejemplo de uso
def main():
    cuenta = CuentaBancaria("Amy", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)

if __name__ == "__main__":
    main()

class Cuenta():
    def __init__(self, Saldo):
        self.Saldo = Saldo;

    def SaldoActual(self):
        return (f"Saldo actual: {self.Saldo}");

    def RetirarSaldo(self, Retiro):
        Saldo = self.Saldo - Retiro;
        return Cuenta(Saldo);

Prueba = Cuenta(1000);
print(f"{Prueba.SaldoActual()}");
Resta = Prueba.RetirarSaldo(100);
print(f"{Resta.SaldoActual()}");
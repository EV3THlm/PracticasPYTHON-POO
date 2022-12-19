class Transferencia():
    def __init__(self, Nombre, Saldo, Edad):
        self.Nombre = Nombre;
        self.Saldo = Saldo;
        self.Edad = Edad;

    # Transferir saldo
    def Poner(self, SaldoTransferir):
        Saldo = (self.Saldo + SaldoTransferir);
        return Transferencia(self.Nombre, Saldo, self.Edad);
    
    def Quitar(self, SaldoTransferir):
        Saldo = (self.Saldo - SaldoTransferir);
        return Transferencia(self.Nombre, Saldo, self.Edad);
    
    # Print Datos
    def MostrarDatos(self):
        print(f"Nombre: {self.Nombre}");
        print(f"Saldo: {self.Saldo}");
        print(f"Edad: {self.Edad}");
    
def main():
    Persona1 = Transferencia("Ebeth", 500, 21);
    Persona2 = Transferencia("Rene", 100, 20);

    Persona1.MostrarDatos();
    print("\n");
    Persona2.MostrarDatos();
    print("\n");
    SalTransferir = int (input("Ingresa saldo a transferir: "));
    NuevoSaldo = Persona1.Quitar(SalTransferir); # Add Saldo
    SaldoQuitado = Persona2.Poner(SalTransferir);
    print("\n");
    print(f"Nuevo saldo de {Persona1.Nombre}: {NuevoSaldo.Saldo}");
    print(f"Nuevo saldo de {Persona2.Nombre}: {SaldoQuitado.Saldo}");

if __name__ == "__main__":
    main();

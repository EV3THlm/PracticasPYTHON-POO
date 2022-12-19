class Fraccion():
    def __init__(self, Numerador, Denominador):
        self.Numerador = Numerador;
        self.Denominador = Denominador;
    
    def MostrarDatos(self):
        print(f"{self.Numerador}/{self.Denominador}");

    def MostrarFraccion(self):
        return(f"{self.Numerador}/{self.Denominador}");
    
    # Operaciones para SUMA
    def Suma(self, Fraccion2):
        Numerador = (self.Numerador * Fraccion2.Denominador) + (self.Denominador * Fraccion2.Numerador);
        Denominador = self.Denominador * Fraccion2.Denominador;
        return Fraccion(Numerador, Denominador);
    
    # Operaciones para RESTA
    def Resta(self, Fraccion2):
        Denominador = self.Denominador * Fraccion2.Denominador;
        Numerador = (Fraccion2.Denominador * self.Numerador) - (self.Denominador * Fraccion2.Numerador);
        return Fraccion(Numerador, Denominador)

    # Operaciones para MULTIPLICACIONES
    def Multiplicacion(self, Fraccion2):
        Numerador = self.Numerador * Fraccion2.Numerador;
        Denominador = self.Denominador * Fraccion2.Denominador;
        return Fraccion(Numerador, Denominador);
    
    # Operaciones para DIVICION
    def Divicion(self, Fraccion2):
        Numerador = self.Numerador * Fraccion2.Denominador;
        Denominador = self.Denominador * Fraccion2.Numerador;
        return Fraccion(Numerador, Denominador);

# Bloque principal
def main():
    # Objeto
    Numerador1 = int (input("Ingresa el numerador 1: "));
    Denominador1 = int (input("Ingresa el denominador 1: "));
    print("\n");
    Numerador2 = int (input ("Ingresa el numerador 2: "));
    Denominador2 = int (input("Ingresa el denominador 2: "));
    Fraccion1 = Fraccion(Numerador1, Denominador1);
    Fraccion2 = Fraccion(Numerador2, Denominador2);
    ResultadoSuma = Fraccion1.Suma(Fraccion2)
    Resultado = Fraccion1.Multiplicacion(Fraccion2)
    Resultado2 = Fraccion1.Resta(Fraccion2);
    Resultado3 = Fraccion1.Divicion(Fraccion2);
    #Resultado.MostrarDatos();
    print(f"{Fraccion1.MostrarFraccion()} + {Fraccion2.MostrarFraccion()} = {ResultadoSuma.MostrarFraccion()}");
    print(f"{Fraccion1.MostrarFraccion()} - {Fraccion2.MostrarFraccion()} = {Resultado2.MostrarFraccion()}");
    print(f"{Fraccion1.MostrarFraccion()} * {Fraccion2.MostrarFraccion()} = {Resultado.MostrarFraccion()}");
    print(f"{Fraccion1.MostrarFraccion()} / {Fraccion2.MostrarFraccion()} = {Resultado3.MostrarFraccion()}");

if __name__ == "__main__":
    main();

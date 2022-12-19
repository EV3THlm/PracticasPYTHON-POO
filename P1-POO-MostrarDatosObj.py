class Persona():
    def __init__(self, Nombre, ApellidoP, ApellidoM, Edad):
        self.Nombre = Nombre;
        self.ApellidoP = ApellidoP;
        self.ApellidoM = ApellidoM;
        self.Edad = Edad;

    def mostrarDatos(self):
        print(f"\nNombre: {self.Nombre} {self.ApellidoP} {self.ApellidoM}");
        print(f"Edad: {self.Edad}");

def main():
    Persona1 = Persona("Ebeth", "Mejia", "Chavez", 22);
    Persona2 = Persona("Emily", "Lopez", "Mendoza", 23);

    Persona1.mostrarDatos();
    Persona2.mostrarDatos();

if __name__ == "__main__":
    main();

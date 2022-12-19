class Persona():
    def __init__(self, Nombre, Apellido, Edad):
        self.Nombre = Nombre;
        self.Apellido = Apellido;
        self.Edad = Edad;
    
    def getEdad(self):
        if self.Edad >= 18:
            print(f"{self.Nombre} es Mayor de edad");
        if self.Edad <= 17:
            print(f"{self.Nombre} es Menor de edad");
    
    # Funcion cambiar nombre
    def changeName(self, NuevoNombre):
        self.Nombre = NuevoNombre;
        print(f"El nombre cambio a: {self.Nombre}");
# Creamos el objeto
Valeria = Persona("Valeria", "Garcia", 18);

# Decimos que nuevo nombre queremos agregar al objeto
Valeria.changeName("Silvana");

# llamamos el objeto
Valeria.getEdad();
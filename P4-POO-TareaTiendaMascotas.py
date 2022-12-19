"""
    Crear el diagrama de clases para una tienda de mascotas
    Perros, Gatos, (Agregar 2 animales minimo) y Clientes

    Identificar ATRIBUTOS Y FUNCIONES (Metodos)
"""

# Clase Persona
class Persona():
    
    def __init__(self, Nombre, Apellido, Edad):
        self.Nombre = Nombre;
        self.Apellido = Apellido;
        self.Edad = Edad;

# Heredamos atributos de una persona
class Cliente(Persona):

    # Restringimos la edad de los cientes para la adopcion
    def getEdad(self):
        if self.Edad >= 18:
            return True;
        if self.Edad <= 18:
            return False

    def Nombre(self):
        return self.Nombre;
    def Apellido(self):
        return self.Apellido;

class Animal():
    def __init__(self, Nombre, Color, Talla, Edad):
        self.Nombre = Nombre;
        self.Color = Color;
        self.Talla = Talla;
        self.Edad = Edad;

# Extendemos PERRO de Clase Animal
class Perro(Animal):
    def Nombre(self):
        return self.Nombre;
    def Color(self):
        return self.Color;
    def Talla(self):
        return self.Talla;
    def Edad(self):
        return self.Edad;

class Gato(Animal):
    def Nombre(self):
        return self.Nombre;
    def Color(self):
        return self.Color;
    def Talla(self):
        return self.Talla;
    def Edad(self):
        return self.Edad;


# Creamos un cliente
Nombre = str (input("Ingresa tu nombre: "));
Apellido = str (input("Ingresa tu apellido: "));
Edad = int (input("Ingresa tu edad: "));
print("\n")
Ebeth = Cliente(Nombre, Apellido, Edad);


# Bloque principal
print("##__ TIENDA DE MASCOTAS __##", "\n");
if Ebeth.getEdad() == False:
    print(f"¡Lo siento! Sr. {Ebeth.Nombre}, tiene que ser mayor de edad para adoptar una mascota", "\n");
if Ebeth.getEdad() == True:
    print("## ¿QUE QUISIERA ADOPTAR? ## \n");
    print("1) Perro");
    print("2) Gato");
    menu = int (input(">>: "));
    print("\n")

    # Si eligio un perro
    if (menu == 1):
        Nombre = str (input("Ingrese el nombre de su nueva mascota: "));
        print("\n")

        # Creamos el objeto perro con el nombre que el cliente quiere
        Perrito = Perro(Nombre, "Cafe", "Mediana", "8 Meses");
        print(f"!FELICIDADES!, Sr. {Ebeth.Nombre}, Muchas gracias por su adopcion \n")
        print("Conozca a su nuevo amigo: \n");
        print(f"Adoptaste a {Perrito.Nombre}, \nEs talla {Perrito.Talla}, \nTiene {Perrito.Edad} de edad.", ); 






# Creamos un objeto perro
#Bimmo = Perro("Bimmo", "Cafe", "MEDIANA", "8 meses")

# Llamamos objetos
#print(f"El perro se llama: {Bimmo.Nombre}")
class Autobuces():
    
    # Atributos principales
    def __init__(self, Ruta, NombreChofer, Pasajeros):
        self.Ruta = Ruta;
        self.NombreChofer = NombreChofer;
        self.Pasajeros = Pasajeros;

    # Metodo para mostrar datos
    def MostrarDatos(self):
        print(f"Ruta: {self.Ruta}");
        print(f"Chofer: {self.NombreChofer}");
        print(f"Pasajeros: {self.Pasajeros}");
        print("\n");

    # Metodo para subir pasajeros
    def addPasajeros(self, Pasajeros):
        self.Pasajeros += Pasajeros;
        print(f"Se subio: {Pasajeros} pasajero\n");
    
    # Metodo para bajar pasajeros
    def delatePasajeros(self, Pasajeros):
        self.Pasajeros -= Pasajeros
        print(f"Se bajo: {Pasajeros} Pasajeros\n");

# Objeto RUTA 1
Ruta1 = Autobuces(45,"Milaeso", 10);
Ruta2 = Autobuces(15, "Chuleta", 2);

Ruta1.MostrarDatos(); # Mostramos los datos de la ruta1
Ruta1.addPasajeros(5);
Ruta1.MostrarDatos();

Ruta1.delatePasajeros(1);
Ruta1.MostrarDatos();

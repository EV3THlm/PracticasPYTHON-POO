# Realizar un programa que calcule el promedio de un ALUMNO
class Alumno():
    def __init__(self, Nombre, Apellido, NoControl, Semestre, Carrera):
        self.Nombre = Nombre;
        self.Apellido = Apellido;
        self.NoControl = NoControl;
        self.Semestre = Semestre;
        self.Carrera = Carrera;

    # Metodo para mostrar datos
    def MostrarDatos(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}");
        print(f"No. Control: {self.NoControl}");
        print(f"Semestre: {self.Semestre}");
        print(f"Carrera: {self.Carrera}");

# Class Promedio para calcular por separado
class Promedio(Alumno):
    def __init__(self, Calificacion):
        self.Calificacion = Calificacion;

    # Metodo para calcular el promedio (5 Materias)
    def CalcularPromedio(self, Calificacion2, Calificacion3, Calificacion4, Calificacion5):
        return (self.Calificacion + Calificacion2.Calificacion + Calificacion3.Calificacion + Calificacion4.Calificacion + Calificacion5.Calificacion)/5

# Objeto alumno
Alumno1 = Alumno("Ebeth", "Mejia", 22590434, 1, "Tic's");
Alumno1.MostrarDatos();
print(f"El promedio es: {Alumno1.CalcularPromedio()}");

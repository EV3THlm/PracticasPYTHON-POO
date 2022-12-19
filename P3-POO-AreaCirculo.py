class Circulo():

    pi = 3.1416

    def __init__(self, Radio = 0):
        self.Radio = Radio;
    
    def getArea(self):
        return round(self.pi * self.Radio** 2, 4)

ValorRadio = float (input("Ingresa el valor para el radio: "));
Circulini = Circulo(ValorRadio);
print(f"El area de circulo es: {Circulini.getArea()}");
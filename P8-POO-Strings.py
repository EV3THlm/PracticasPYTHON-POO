class PrintStrings():
    def __init__(self, Cadena):
        self.Cadena = Cadena;

    def PrintString(self):
        print(f"{self.Cadena}");
    def ReturnString(self):
        return (f"{self.Cadena}");

Texto = PrintStrings("¡GoodBye World!");
Texto.PrintString();
print(f"{Texto.ReturnString()}");

from Animal import Animal
class Bovino(Animal):

    def __init__(self):
        self.establo=int
        self.propietario=""
        self.fecha_vacunacion=""

    def pastar(self):
        if self.establo > 5:
            print ("no pastar")
        elif self.establo <=5:
            print("pastar")

    def emitir_sonido(self):
        self.emitir_Sonido = print("Muuu")
 
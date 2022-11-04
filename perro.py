from Animal import Animal



class Perro(Animal):

    def __init__(self):
        self.propietario=""
        self.fecha_vacunacion=""        


    def emitir_Sonido(self,edad):
        if self.edad <=3:
            print ("auf auf")
        elif self.edad >3:
            print ("Gau Gau")


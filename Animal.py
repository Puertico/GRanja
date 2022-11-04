class Animal:
    def __init__(self):
        self.peso=""
        self.edad=int
        self.raza=""
        self.fecha_vacunacion=""
        self.propietario=""

    def correr(self):
        if self.edad >= 5:
         print ("rapido")
        elif self.edad <5:
         print ("lento")

    def emitir_sonido(self):
        pass
    
    def pastar(self):
        pass    

    def obtener_edad(self):
        return self.edad


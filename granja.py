from Animal import Animal
from perro import Perro
from bovino import Bovino

class Granja:

    def __init__(self):
        self.miperro=[]
        self.mibovino=[]
        


    def agregar_perro(self, edad,raza,fecha_vacunacion,propietario,emitir_sonido):
        
        if len(self.miperro)==0:

             perro=Perro()

             perro.edad=edad
             perro.raza=raza
             perro.fecha_vacunacion=fecha_vacunacion
             perro.propietario=propietario
             perro.emitir_Sonido=emitir_sonido
        else:
            pass
    def agregar_bovino(self, edad,raza,fecha_vacunacion,propietario, pastar,emitir_sonido):
        
         if len(self.mibovino)==0:
             bovino=Bovino()

             bovino.edad=edad
             bovino.raza=raza
             bovino.fecha_vacunacion=fecha_vacunacion
             bovino.propietario=propietario
             bovino.emitir_Sonido=emitir_sonido
             bovino.pastar=pastar
         else:
                pass

    def obtener_perro(self):

        self.miperro
    
    def obtener_bovino(self):

        self.mibovino
       
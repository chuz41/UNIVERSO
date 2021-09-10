

class universo: #Clase de la cual heredarán todas las clases. Es como un dios.

    def __init__(self, param10):
        self.param1 = param10
        print("Estamos en la clase UNIVERSO, método init \n")

    def mostrarEstado(self, momentoET):
        self.momentoET = momentoET
        print("Estamos en el método: mostrar estado espacio-temporal")
        return momentoET    


#universoC137 = UNIVERSO(137)

#print(universoC137.param1)








    #end

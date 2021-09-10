
from universo import universo
from timeGen import timeGen
from genFisMag import genFisMag
from classRealidad import realidadGeneral


universoC137 = universo(137)
gravedad = 0
print(universoC137.param1)


print(universoC137.mostrarEstado(200))


#Variables fundamentales:
varFisicas = genFisMag(110)

print(varFisicas.gravedad.keys())
print(varFisicas.gravedad.items())


#Primera ley física: El tiempo corre hacia adelante. 

print("\nHoy es: ")
time = timeGen()
print(time)
print("\n")

#aquí, se genera el espacio y todas las demás leyes de la física, 
#incluyendo la materia, el espacio y la energía. Estas se irán 
#implementando cuando se valla necesitando.

#En la siguiente función, se supone que empieza a correr un trozo de realidad espacio-temporal.
#Una conciencia (O muchas!!). 

while time > 0:
    print("Welcome to a part of the reality.")
    #Se procede a crear una realidad.
    paginaWeb = realidadGeneral("PagWeb")
    print(paginaWeb.primerParam)

    break
















#end

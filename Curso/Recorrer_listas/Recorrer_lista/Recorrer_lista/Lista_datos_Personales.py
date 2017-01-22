############################################
# ---------------> Python 3 <---------------
############################################


############################################
# LISTAS
# Cree una lista destinada a guardar datos 
# de personas, como nombre, edad etc.
# Realice operaciones sobre la lista 
# utilizando todos los campos de la tabla 
# del punto 7.1.
############################################
dataList = []
members = [['Juan', 23,'pintor'],['Pepe', 28,'programador'],
           ['Carlos', 38,'disenador'],['Roberto', 22,'arquitecto'],
           ['Esteban', 37,'ingeniero'],['Pedro', 31,'vendedor'],
           ['Pablo', 34,'carpintero'],['Raul', 23,'programador'],
           ['Guillermo', 25,'ingeniero'],['Federico', 24,'disenador']]

L = []
numero_de_personas = 1

for i in range(numero_de_personas):
    nombre = eval(input('Ingrese nombre de la persona: '))
    edad = eval(input(' Ingrese edad de la persona: '))
    profesion = eval(input(' Ingrese profesion de la persona: '))

    L.append([])
    L[i].append(nombre)
    L[i].append(edad)
    L[i].append(profesion)

print ('\nLista cargada: ', L)
input()

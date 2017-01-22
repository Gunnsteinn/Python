############################################
# ---------------> Python 3 <---------------
############################################


############################################
# LISTAS
# Recorremos una lista
############################################
peliculas = ["pelicula1", "pelicula2", "pelicula3"]
print(peliculas)
print(peliculas[0])
print(len(peliculas))
# Con append agregamos datos al final de una lista
peliculas.append("pelicula4")
print(peliculas)
# Con pop removemos el �ltimo dato de una lista
peliculas.pop()
print(peliculas)
# Con extend agregamos un grupo de datos al final de la lista
peliculas.extend(["pelicula4", "pelicula5"])
print(peliculas)
# Con remove removemos un dato espec�fico de la lista
peliculas.remove("pelicula4")
print(peliculas)
# Con insert insertamos un dato en un lugar especifico de la lista
peliculas.insert(0, "pelicula0")
print(peliculas)
input()
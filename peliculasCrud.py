#--------------------------------------------------
# FUNCIONES CRUD PARA PELICULAS
#--------------------------------------------------
#Funcion para agregar película (Crud)
def agregarPelicula(peliculas_matriz):
    print("Agregar Nueva Película:")
    nuevo_id = peliculas_matriz[-1][0] + 1
    titulo = input("Ingrese Título: ")
    genero = input("Ingrese Género: ")
    duracion = int(input("Ingrese Duración en Minutos: "))
    clasificacion = input("Ingrese Clasificación: ")
    peliculas_matriz.append([nuevo_id, titulo, genero, duracion, clasificacion])
    print(f"¡Película '{titulo}' agregada con éxito!")

#--------------------------------------------------

#Funcion para leer películas (cRud)
def leerPelicula(peliculas_matriz):
    print("Consultar Película por ID:")
    id_buscar = int(input("Ingrese ID de la Película a Consultar: "))
    seEncontro = False
    for pelicula in peliculas_matriz[1:]:
        if pelicula[0] == id_buscar:
            print(f"Película Encontrada: ID: {pelicula[0]}, Título: {pelicula[1]}, Género: {pelicula[2]}, Duración: {pelicula[3]} min, Clasificación: {pelicula[4]}")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

#--------------------------------------------------

#Funcion para actualizar película (crUd)
def actualizarPelicula(peliculas_matriz):
    print("Actualizar Película Existente:")
    id_buscar = int(input("Ingrese ID de la Película a Actualizar: "))
    seEncontro = False
    for pelicula in peliculas_matriz[1:]:
        if pelicula[0] == id_buscar:
            print(f"Película Encontrada: {pelicula[1]}")
            nuevo_titulo = input("Ingrese Nuevo Título (dejar en blanco para no cambiar): ")
            nuevo_genero = input("Ingrese Nuevo Género (dejar en blanco para no cambiar): ")
            nuevo_duracion = input("Ingrese Nueva Duración en Minutos (dejar en blanco para no cambiar): ")
            nuevo_clasificacion = input("Ingrese Nueva Clasificación (dejar en blanco para no cambiar): ")

            if nuevo_titulo:
                pelicula[1] = nuevo_titulo
            if nuevo_genero:
                pelicula[2] = nuevo_genero
            if nuevo_duracion:
                pelicula[3] = int(nuevo_duracion)
            if nuevo_clasificacion:
                pelicula[4] = nuevo_clasificacion

            print(f"¡Película ID {id_buscar} actualizada con éxito!")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

#--------------------------------------------------

#Funcion para eliminar película (cruD)
def eliminarPelicula(peliculas_matriz):
    print("Eliminar Película Existente:")
    id_buscar = int(input("Ingrese ID de la Película a Eliminar: "))
    seEncontro = False
    for i, pelicula in enumerate(peliculas_matriz[1:], start=1):
        if pelicula[0] == id_buscar:
            confirmacion = input(f"¿Está seguro que desea eliminar la película '{pelicula[1]}'? (s/n): ")
            if confirmacion.lower() == 's':
                del peliculas_matriz[i]
                print(f"¡Película ID {id_buscar} eliminada con éxito!")
            else:
                print("Operación cancelada.")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

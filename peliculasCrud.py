#--------------------------------------------------
#Funcion para agregar película (Crud)
#--------------------------------------------------
# FUNCIONES CRUD PARA PELICULAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarPelicula(peliculas_lista):
    print("Agregar Nueva Película:")
    # Obtener el ID más alto y sumar 1
    nuevo_id = max([p['ID_Pelicula'] for p in peliculas_lista]) + 1 if peliculas_lista else 1
    titulo = input("Ingrese Título: ")
    genero = input("Ingrese Género: ")
    #falta
    duracion = int(input("Ingrese Duración en Minutos: "))
    clasificacion = input("Ingrese Clasificación: ")
    
    nueva_pelicula = {
        'ID_Pelicula': nuevo_id,
        'Titulo': titulo,
        'Genero': genero,
        'Duracion_min': duracion,
        'Clasificacion': clasificacion
    }
    peliculas_lista.append(nueva_pelicula)
    print(f"Película '{titulo}' agregada.")

def leerPeliculaPorId(peliculas_lista):
    print("Consultar Película por ID:")
    try:
        id_buscar = int(input("Ingrese ID de la Película a Consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    pelicula_encontrada = None
    i = 0
    while i < len(peliculas_lista) and pelicula_encontrada is None:
        if peliculas_lista[i]['ID_Pelicula'] == id_buscar:
            pelicula_encontrada = peliculas_lista[i]
        i += 1
    
    if pelicula_encontrada:
        print(f"Película Encontrada: ID: {pelicula_encontrada['ID_Pelicula']}, Título: {pelicula_encontrada['Titulo']}, Género: {pelicula_encontrada['Genero']}, Duración: {pelicula_encontrada['Duracion_min']} min, Clasificación: {pelicula_encontrada['Clasificacion']}")
    else:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

def leerPeliculaPorNombre(peliculas_lista):
    print("Buscar Película por Nombre:")
    nombre_buscar = input("Ingrese el Nombre o parte del Nombre de la Película: ").lower()
    peliculas_encontradas = [p for p in peliculas_lista if nombre_buscar in p['Titulo'].lower()]
    
    if peliculas_encontradas:
        print("Películas Encontradas:")
        for pelicula in peliculas_encontradas:
            print(f"ID: {pelicula['ID_Pelicula']}, Título: {pelicula['Titulo']}, Género: {pelicula['Genero']}, Duración: {pelicula['Duracion_min']} min, Clasificación: {pelicula['Clasificacion']}")
    else:
        print(f"No se encontraron películas que coincidan con '{nombre_buscar}'.")

def actualizarPelicula(peliculas_lista):
    print("Actualizar Película Existente:")
    try:
        id_buscar = int(input("Ingrese ID de la Película a Actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    pelicula_a_actualizar = None
    i = 0
    while i < len(peliculas_lista) and pelicula_a_actualizar is None:
        if peliculas_lista[i]['ID_Pelicula'] == id_buscar:
            pelicula_a_actualizar = peliculas_lista[i]
        i += 1

    if pelicula_a_actualizar:
        print(f"Película Encontrada: {pelicula_a_actualizar['Titulo']}")
        nuevo_titulo = input("Ingrese Nuevo Título (dejar en blanco para no cambiar): ")
        nuevo_genero = input("Ingrese Nuevo Género (dejar en blanco para no cambiar): ")
        nuevo_duracion = input("Ingrese Nueva Duración en Minutos (dejar en blanco para no cambiar): ")
        nuevo_clasificacion = input("Ingrese Nueva Clasificación (dejar en blanco para no cambiar): ")

        if nuevo_titulo:
            pelicula_a_actualizar['Titulo'] = nuevo_titulo
        if nuevo_genero:
            pelicula_a_actualizar['Genero'] = nuevo_genero
        if nuevo_duracion:
            #falta
            pelicula_a_actualizar['Duracion_min'] = int(nuevo_duracion)
        if nuevo_clasificacion:
            pelicula_a_actualizar['Clasificacion'] = nuevo_clasificacion

        print(f"Película ID {id_buscar} actualizada.")
    else:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

def eliminarPelicula(peliculas_lista):
    print("Eliminar Película Existente:")
    try:
        id_buscar = int(input("Ingrese ID de la Película a Eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    indice_a_eliminar = -1
    i = 0
    while i < len(peliculas_lista) and indice_a_eliminar == -1:
        if peliculas_lista[i]['ID_Pelicula'] == id_buscar:
            indice_a_eliminar = i
        i += 1
    
    if indice_a_eliminar != -1:
        pelicula = peliculas_lista[indice_a_eliminar]
        confirmacion = input(f"¿Está seguro que desea eliminar la película '{pelicula['Titulo']}'? (s/n): ").lower()
        if confirmacion == 's':
            peliculas_lista.pop(indice_a_eliminar)
            print(f"Película ID {id_buscar} eliminada.")
        else:
            print("Operación cancelada.")
    else:
        print(f"No se encontró ninguna película con ID {id_buscar}.")

# --- TUPLAS ---
def obtener_info_basica_pelicula(peliculas_lista, id_buscar):
    """
    Busca una película por su ID y devuelve sus datos principales en una tupla.
    Retorna: (Titulo, Genero, Clasificacion) o None si no la encuentra.
    """
    pelicula_encontrada = None
    for p in peliculas_lista:
        if p['ID_Pelicula'] == id_buscar:
            pelicula_encontrada = p
            break
    
    if pelicula_encontrada:
        info = (
            pelicula_encontrada['Titulo'], 
            pelicula_encontrada['Genero'], 
            pelicula_encontrada['Clasificacion']
        )
        return info
    else:
        return None
    
# SLICING 2 [:n] FALTA PONER EN MENU CON 
#try:
#    leerPrimerasNPeliculas(peliculas, cantidad)
#except ValueError as e:
#    print(e)


def leerPrimerasNPeliculas(peliculas_lista, n):
    if len(peliculas_lista)<n:
        raise ValueError("No hay suficientes peliculas para mostrar.")
    print(f"Primeras {n} Peliculas Agregadas:")
    primeras_n_peliculas = peliculas_lista[:n]
    for pelicula in primeras_n_peliculas:
        print(f"ID: {pelicula['ID_Pelicula']}, Título: {pelicula['Titulo']}, Género: {pelicula['Genero']}, Duración: {pelicula['Duracion_min']} min, Clasificación: {pelicula['Clasificacion']}")
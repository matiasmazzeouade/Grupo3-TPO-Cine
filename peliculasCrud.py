#--------------------------------------------------
# Funcion para agregar película (Crud)
#--------------------------------------------------
# FUNCIONES CRUD PARA PELICULAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarPelicula(peliculas_lista):
    print("Agregar Nueva Película:")
    nuevo_id = max([p['ID_Pelicula'] for p in peliculas_lista]) + 1 if peliculas_lista else 1

    # --- Validar título ---
    titulo = input("Ingrese Título: ").strip()
    if not titulo or len(titulo) < 2:
        print("Error: El título no puede estar vacío y debe tener al menos 2 caracteres.")
        return

    # --- Validar género ---
    genero = input("Ingrese Género: ").strip()
    if not genero:
        print("Error: El género no puede estar vacío.")
        return

    # --- Validar duración ---
    try:
        duracion = int(input("Ingrese Duración en Minutos: "))
        if duracion <= 0:
            print("Error: La duración debe ser un número positivo.")
            return
    except ValueError:
        print("Error: La duración debe ser un número entero.")
        return

    # --- Validar clasificación ---
    clasificacion = input("Ingrese Clasificación (ATP, +13, +16, +18): ").strip().upper()
    if not clasificacion:
        print("Error: La clasificación no puede estar vacía.")
        return

    # Clasificaciones permitidas opcionalmente
    permitidas = {"ATP", "+13", "+16", "+18"}
    if clasificacion not in permitidas:
        print("Error: Clasificación inválida. Debe ser ATP, +13, +16 o +18.")
        return

    nueva_pelicula = {
        'ID_Pelicula': nuevo_id,
        'Titulo': titulo,
        'Genero': genero,
        'Duracion_min': duracion,
        'Clasificacion': clasificacion
    }

    peliculas_lista.append(nueva_pelicula)
    print(f"Película '{titulo}' agregada correctamente.")

# FUNCIÓN RECURSIVA
def _buscar_pelicula_recursiva(lista, id_buscar):
    if not lista:
        return None
    
    if lista[0]['ID_Pelicula'] == id_buscar:
        return lista[0]

    return _buscar_pelicula_recursiva(lista[1:], id_buscar)

def leerPeliculaPorId(peliculas_lista):
    print("Consultar Película por ID:")
    try:
        id_buscar = int(input("Ingrese ID de la Película a Consultar: "))
    except ValueError: 
        print("Error: El ID debe ser un número entero.")
        return
    
    pelicula_encontrada = _buscar_pelicula_recursiva(peliculas_lista, id_buscar)
    
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
    
    pelicula_a_actualizar = _buscar_pelicula_recursiva(peliculas_lista, id_buscar)

    if not pelicula_a_actualizar:
        print(f"No se encontró ninguna película con ID {id_buscar}.")
        return
    
    print(f"Película Encontrada: {pelicula_a_actualizar['Titulo']}")

    nuevo_titulo = input("Ingrese Nuevo Título (dejar en blanco para no cambiar): ").strip()
    nuevo_genero = input("Ingrese Nuevo Género (dejar en blanco para no cambiar): ").strip()
    nuevo_duracion_str = input("Ingrese Nueva Duración (minutos) (dejar en blanco para no cambiar): ").strip()
    nuevo_clasificacion = input("Ingrese Nueva Clasificación (ATP, +13, +16, +18) (dejar en blanco para no cambiar): ").strip().upper()

    # --- Validar título ---
    if nuevo_titulo:
        if len(nuevo_titulo) < 2:
            print("Error: El título debe tener al menos 2 caracteres.")
            return
        pelicula_a_actualizar['Titulo'] = nuevo_titulo

    # --- Validar género ---
    if nuevo_genero:
        pelicula_a_actualizar['Genero'] = nuevo_genero

    # --- Validar duración ---
    if nuevo_duracion_str:
        try:
            nueva_duracion = int(nuevo_duracion_str)
            if nueva_duracion <= 0:
                print("Error: La duración debe ser un número positivo.")
                return
            pelicula_a_actualizar['Duracion_min'] = nueva_duracion
        except ValueError:
            print("Error: La duración debe ser un número entero.")
            return

    # --- Validar clasificación ---
    if nuevo_clasificacion:
        permitidas = {"ATP", "+13", "+16", "+18"}
        if nuevo_clasificacion not in permitidas:
            print("Error: Clasificación inválida. Debe ser ATP, +13, +16 o +18.")
            return
        pelicula_a_actualizar['Clasificacion'] = nuevo_clasificacion

    print(f"Película ID {id_buscar} actualizada correctamente.")

def eliminarPelicula(peliculas_lista, funciones_lista, reservas_lista):
    print("Eliminar Película Existente:")
    try:
        id_buscar = int(input("Ingrese ID de la Película a Eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    pelicula = _buscar_pelicula_recursiva(peliculas_lista, id_buscar)

    if not pelicula:
        print(f"No existe película con ID {id_buscar}.")
        return

    confirm = input(f"¿Eliminar '{pelicula['Titulo']}' y TODAS sus funciones y reservas? (s/n): ").lower()
    if confirm != "s":
        print("Cancelado.")
        return

    # Funciones asociadas
    funciones_asociadas = [f for f in funciones_lista if f['ID_Pelicula'] == id_buscar]
    ids_funciones = [f['ID_Funcion'] for f in funciones_asociadas]

    # Eliminar funciones
    funciones_lista[:] = [f for f in funciones_lista if f['ID_Pelicula'] != id_buscar]

    # Eliminar reservas asociadas
    reservas_lista[:] = [r for r in reservas_lista if r['ID_Funcion'] not in ids_funciones]

    # Eliminar película
    peliculas_lista.remove(pelicula)

    print("Película eliminada en cascada correctamente.")

# --- TUPLAS ---
def obtener_info_basica_pelicula(peliculas_lista, id_buscar):
    """
    Busca una película por su ID y devuelve sus datos principales en una tupla.
    Retorna: (Titulo, Genero, Clasificacion) o None si no la encuentra.
    """
    pelicula_encontrada = _buscar_pelicula_recursiva(peliculas_lista, id_buscar)
    
    if pelicula_encontrada:
        info = (
            pelicula_encontrada['Titulo'], 
            pelicula_encontrada['Genero'], 
            pelicula_encontrada['Clasificacion']
        )
        return info
    else:
        return None

# --- SLICING ---
def leerPrimerasNPeliculas(peliculas_lista, n):
    if n <= 0:
        raise ValueError("La cantidad debe ser un número positivo.")
    if len(peliculas_lista) < n:
        raise ValueError("No hay suficientes peliculas para mostrar.")
    
    print(f"Primeras {n} Peliculas Agregadas:")
    # Esta es la línea que usa Slicing
    primeras_n_peliculas = peliculas_lista[:n] 
    for pelicula in primeras_n_peliculas:
        print(f"ID: {pelicula['ID_Pelicula']}, Título: {pelicula['Titulo']}, Género: {pelicula['Genero']}, Duración: {pelicula['Duracion_min']} min, Clasificación: {pelicula['Clasificacion']}")

def menu_peliculas(peliculas_lista, funciones_lista, reservas_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Películas ---")
        print("1. Agregar")
        print("2. Consultar por ID")
        print("3. Consultar por nombre")
        print("4. Actualizar")
        print("5. Eliminar (cascada)")
        print("6. Ver primeras N")
        print("7. Info básica (tupla)")
        print("x. Volver")

        op = input("Seleccione: ").lower()

        if op == "1":
            agregarPelicula(peliculas_lista)

        elif op == "2":
            leerPeliculaPorId(peliculas_lista)

        elif op == "3":
            leerPeliculaPorNombre(peliculas_lista)

        elif op == "4":
            actualizarPelicula(peliculas_lista)

        elif op == "5":
            eliminarPelicula(peliculas_lista, funciones_lista, reservas_lista)

        elif op == "6":
            try:
                n = int(input("¿Cantidad?: "))
                leerPrimerasNPeliculas(peliculas_lista, n)
            except Exception as e:
                print("Error:", e)

        elif op == "7":
            try:
                pid = int(input("ID?: "))
                print(obtener_info_basica_pelicula(peliculas_lista, pid))
            except:
                print("Error")

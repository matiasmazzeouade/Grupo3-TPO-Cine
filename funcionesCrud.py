from datetime import datetime

#--------------------------------------------------
# FUNCIONES CRUD PARA FUNCIONES (CON DICCIONARIOS)
#--------------------------------------------------

# --- Funciones auxiliares ---
def validar_horario_manual(horario):
    try:
        partes = horario.split(":")
        if len(partes) != 2:
            return False

        h, m = partes

        if not (h.isdigit() and m.isdigit()):
            return False

        h = int(h)
        m = int(m)

        if h < 0 or h > 23:
            return False
        if m < 0 or m > 59:
            return False

        return True
    except:
        return False


def convertir_a_minutos(horario_str):
    horas, minutos = map(int, horario_str.split(':'))
    return horas * 60 + minutos

def sala_ocupada_manual(id_sala, horario_str, fecha, id_pelicula, peliculas_lista, funciones_lista):
    pelicula_nueva = None
    for p in peliculas_lista:
        if p['ID_Pelicula'] == id_pelicula:
            pelicula_nueva = p
            break
            
    if not pelicula_nueva: return False

    duracion_nueva = pelicula_nueva['Duracion_min']
    inicio_nuevo = convertir_a_minutos(horario_str)
    fin_nuevo = inicio_nuevo + duracion_nueva

    esta_ocupada = False
    i = 0
    while i < len(funciones_lista) and not esta_ocupada:
        funcion = funciones_lista[i]
        if funcion['ID_Sala'] == id_sala and funcion['Fecha'] == fecha:
            pelicula_existente = None
            for p in peliculas_lista:
                if p['ID_Pelicula'] == funcion['ID_Pelicula']:
                    pelicula_existente = p
                    break
            
            if pelicula_existente:
                duracion_existente = pelicula_existente['Duracion_min']
                inicio_existente = convertir_a_minutos(funcion['Horario'])
                fin_existente = inicio_existente + duracion_existente
                if inicio_nuevo < fin_existente and fin_nuevo > inicio_existente:
                    esta_ocupada = True
        i += 1
    return esta_ocupada

# --- Funciones CRUD ---
def agregarFuncion(funciones_lista, peliculas_lista, salas_lista):
    print("Agregar Nueva Función:")
    nuevo_id = max([f['ID_Funcion'] for f in funciones_lista]) + 1 if funciones_lista else 501
    try:
        pelicula_id = int(input("Ingrese ID de la Película: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    pelicula_existe = False
    for p in peliculas_lista:
        if p['ID_Pelicula'] == pelicula_id:
            pelicula_existe = True
            break
    if not pelicula_existe:
        print(f"No existe ninguna película con ID {pelicula_id}.")
        return
    
    try:
        sala_id = int(input("Ingrese ID de Sala: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    sala_existe = False
    for s in salas_lista:
        if s['ID_Sala'] == sala_id:
            sala_existe = True
            break
    if not sala_existe:
        print(f"No existe ninguna sala con ID {sala_id}.")
        return
    
    horario = input("Ingrese Horario (HH:MM): ")
    if not validar_horario_manual(horario):
        print("El formato de horario es inválido. Use HH:MM en formato 24 horas.")
        return
    
    # --- Validar fecha ---
    fecha_str = input("Ingrese Fecha (YYYY-MM-DD): ").strip()
    
    if not fecha_str:
        print("Error: La fecha no puede estar vacía.")
        return
    
    try:
        fecha_parsed = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")
        return
    
    # Validación opcional (recomendada para sumar puntos):
    # Evitar funciones en fechas pasadas
    from datetime import date
    if fecha_parsed < date.today():
        print("Error: No se puede registrar una función en una fecha pasada.")
        return
    
    # Convertir a ISO para el diccionario
    fecha = fecha_parsed.isoformat()
    
    if sala_ocupada_manual(sala_id, horario, fecha, pelicula_id, peliculas_lista, funciones_lista):
        print(f"La sala {sala_id} ya tiene una función que se superpone en ese horario y fecha.")
        return

    nueva_funcion = {
        'ID_Funcion': nuevo_id,
        'ID_Pelicula': pelicula_id,
        'ID_Sala': sala_id,
        'Horario': horario,
        'Fecha': fecha
    }
    funciones_lista.append(nueva_funcion)
    print(f"Función para la película ID {pelicula_id} en la sala {sala_id} agregada.")

def leerFuncionPorId(funciones_lista):
    print("Consultar Función por ID:")
    try:
        id_buscar = int(input("Ingrese ID de la Función a Consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    funcion_encontrada = None
    for f in funciones_lista:
        if f['ID_Funcion'] == id_buscar:
            funcion_encontrada = f
            break
    
    if funcion_encontrada:
        print(f"Función Encontrada: ID: {funcion_encontrada['ID_Funcion']}, ID Película: {funcion_encontrada['ID_Pelicula']}, ID Sala: {funcion_encontrada['ID_Sala']}, Horario: {funcion_encontrada['Horario']}, Fecha: {funcion_encontrada['Fecha']}")
    else:
        print(f"No se encontró ninguna función con ID {id_buscar}.")

def leerFuncionesPorFecha(funciones_lista):
    print("Buscar Funciones por Fecha:")
    fecha_buscar_str = input("Ingrese la Fecha (YYYY-MM-DD): ")
    try:
        fecha_buscar = datetime.strptime(fecha_buscar_str, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("Formato de fecha inválido.")
        return
    
    seEncontro = False
    for funcion in funciones_lista:
        if funcion['Fecha'] == fecha_buscar:
            print(f"ID: {funcion['ID_Funcion']}, ID Película: {funcion['ID_Pelicula']}, ID Sala: {funcion['ID_Sala']}, Horario: {funcion['Horario']}")
            seEncontro = True
    if not seEncontro:
        print(f"No se encontraron funciones para la fecha {fecha_buscar}.")

def actualizarFuncionPorId(funciones_lista, peliculas_lista, salas_lista):
    print("Actualizar Función Existente:")
    try:
        id_buscar = int(input("Ingrese ID de la Función a Actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    # Buscar función
    funcion_a_actualizar = next((f for f in funciones_lista if f['ID_Funcion'] == id_buscar), None)

    if not funcion_a_actualizar:
        print(f"No se encontró ninguna función con ID {id_buscar}.")
        return

    print(f"Función encontrada — Película: {funcion_a_actualizar['ID_Pelicula']}, "
          f"Sala: {funcion_a_actualizar['ID_Sala']}, "
          f"Horario: {funcion_a_actualizar['Horario']}")

    # --- Nuevos datos ---
    nuevo_id_pelicula = input("Nuevo ID de Película (dejar en blanco para no cambiar): ").strip()
    nuevo_id_sala = input("Nuevo ID de Sala (dejar en blanco para no cambiar): ").strip()
    nuevo_horario = input("Nuevo Horario (HH:MM) (dejar en blanco para no cambiar): ").strip()

    # --- Validar y actualizar película ---
    if nuevo_id_pelicula:
        try:
            nuevo_id_pelicula = int(nuevo_id_pelicula)
        except ValueError:
            print("Error: El ID de película debe ser un número entero.")
            return

        pelicula_existe = next((p for p in peliculas_lista if p['ID_Pelicula'] == nuevo_id_pelicula), None)
        if not pelicula_existe:
            print(f"Error: No existe ninguna película con ID {nuevo_id_pelicula}.")
            return

        funcion_a_actualizar['ID_Pelicula'] = nuevo_id_pelicula

    # --- Validar y actualizar sala ---
    if nuevo_id_sala:
        try:
            nuevo_id_sala = int(nuevo_id_sala)
        except ValueError:
            print("Error: El ID de sala debe ser un número entero.")
            return

        sala_existe = next((s for s in salas_lista if s['ID_Sala'] == nuevo_id_sala), None)
        if not sala_existe:
            print(f"Error: No existe ninguna sala con ID {nuevo_id_sala}.")
            return

        # Validar sala corrupta
        if sala_existe['Capacidad'] <= 0 or not sala_existe['Nombre_Sala'].strip():
            print("Error: La sala seleccionada tiene datos inválidos.")
            return

        funcion_a_actualizar['ID_Sala'] = nuevo_id_sala

    # --- Validar y actualizar horario ---
    if nuevo_horario:
        if not validar_horario_manual(nuevo_horario):
            print("Error: El horario debe ser válido y con formato HH:MM.")
            return

        funcion_a_actualizar['Horario'] = nuevo_horario

    print(f"Función ID {id_buscar} actualizada correctamente.")

def eliminarFuncion(funciones_lista, reservas_lista):
    print("Eliminar Función:")
    try:
        id_buscar = int(input("ID de la función: "))
    except ValueError:
        print("Valor inválido.")
        return

    funcion = next((f for f in funciones_lista if f['ID_Funcion'] == id_buscar), None)

    if not funcion:
        print("No existe la función.")
        return

    confirm = input("¿Eliminar función y reservas asociadas? (s/n): ").lower()
    if confirm != "s":
        print("Cancelado.")
        return

    reservas_lista[:] = [r for r in reservas_lista if r['ID_Funcion'] != id_buscar]
    funciones_lista.remove(funcion)

    print("Función y reservas eliminadas.")

def menu_funciones(funciones_lista, peliculas_lista, salas_lista, reservas_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Funciones ---")
        print("1. Agregar")
        print("2. Consultar por ID")
        print("3. Consultar por fecha")
        print("4. Actualizar")
        print("5. Eliminar (cascada)")
        print("x. Volver")

        op = input("Seleccione: ").lower()

        if op == "1":
            agregarFuncion(funciones_lista, peliculas_lista, salas_lista)

        elif op == "2":
            leerFuncionPorId(funciones_lista)

        elif op == "3":
            leerFuncionesPorFecha(funciones_lista)

        elif op == "4":
            actualizarFuncionPorId(funciones_lista, peliculas_lista, salas_lista)

        elif op == "5":
            eliminarFuncion(funciones_lista, reservas_lista)

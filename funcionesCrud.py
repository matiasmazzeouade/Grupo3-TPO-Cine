from datetime import datetime

#--------------------------------------------------
# FUNCIONES CRUD PARA FUNCIONES (CON DICCIONARIOS)
#--------------------------------------------------

# --- Funciones auxiliares ---
def validar_horario_manual(horario):
    try:
        datetime.strptime(horario, '%H:%M')
        return True
    except ValueError:
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
    
    pelicula_id = int(input("Ingrese ID de la Película: "))
    pelicula_existe = False
    for p in peliculas_lista:
        if p['ID_Pelicula'] == pelicula_id:
            pelicula_existe = True
            break
    if not pelicula_existe:
        print(f"No existe ninguna película con ID {pelicula_id}.")
        return
    
    sala_id = int(input("Ingrese ID de Sala: "))
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
    
    fecha_str = input("Ingrese Fecha (YYYY-MM-DD): ")
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("Formato de fecha inválido. Debe ser YYYY-MM-DD.")
        return

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
    id_buscar = int(input("Ingrese ID de la Función a Consultar: "))
    
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
    print("Actualizar Función por ID:")
    id_buscar = int(input("Ingrese ID de la Función a Actualizar: "))
    
    funcion_a_actualizar = None
    for f in funciones_lista:
        if f['ID_Funcion'] == id_buscar:
            funcion_a_actualizar = f
            break

    if funcion_a_actualizar:
        print(f"Función Encontrada: ID Película: {funcion_a_actualizar['ID_Pelicula']}, ID Sala: {funcion_a_actualizar['ID_Sala']}, Horario: {funcion_a_actualizar['Horario']}, Fecha: {funcion_a_actualizar['Fecha']}")
        
        nuevo_horario = input("Ingrese Nuevo Horario (HH:MM) (dejar en blanco para no cambiar): ")
        if nuevo_horario and validar_horario_manual(nuevo_horario):
            funcion_a_actualizar['Horario'] = nuevo_horario
        elif nuevo_horario:
            print("Formato de horario inválido. No se actualizó.")
        
        print(f"Función ID {id_buscar} actualizada.")
    else:
        print(f"No se encontró ninguna función con ID {id_buscar}.")

def eliminarFuncion(funciones_lista):
    print("Eliminar Función Existente:")
    id_buscar = int(input("Ingrese ID de la Función a Eliminar: "))
    
    indice_a_eliminar = -1
    i = 0
    while i < len(funciones_lista) and indice_a_eliminar == -1:
        if funciones_lista[i]['ID_Funcion'] == id_buscar:
            indice_a_eliminar = i
        i += 1

    if indice_a_eliminar != -1:
        confirmacion = input(f"¿Está seguro que desea eliminar la función ID {id_buscar}? (s/n): ").lower()
        if confirmacion == 's':
            funciones_lista.pop(indice_a_eliminar)
            print(f"Función ID {id_buscar} eliminada.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ninguna función con ID {id_buscar}.")
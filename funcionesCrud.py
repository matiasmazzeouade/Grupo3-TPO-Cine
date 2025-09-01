from datetime import datetime
#--------------------------------------------------
# FUNCIONES CRUD PARA FUNCIONES
#--------------------------------------------------

#Funciones auxiliares para funciones
def validar_horario_manual(horario):
    #Valida que el horario esté en formato HH:MM con 24hs.
    if len(horario) != 5 or horario[2] != ":":
        return False
    horas = int(horario[:2])
    minutos = int(horario[3:])
    return 0 <= horas <= 23 and 0 <= minutos <= 59


def convertir_a_minutos(horario: str) -> int:
    #Convierte HH:MM a minutos totales desde las 00:00.
    horas = int(horario[:2])
    minutos = int(horario[3:])
    return horas * 60 + minutos


def sala_ocupada_manual(id_sala, horario_str, fecha, id_pelicula, peliculas_matriz, funciones_matriz):
    #Verifica si la sala ya tiene una función que se superponga.

    # Buscar duración de la película
    duracion = 0
    for pelicula in peliculas_matriz[1:]:
        if pelicula[0] == id_pelicula:
            duracion = pelicula[3]
            break

    inicio_nuevo = convertir_a_minutos(horario_str)
    fin_nuevo = inicio_nuevo + duracion

    for funcion in funciones_matriz[1:]:
        if funcion[2] == id_sala and funcion[4] == fecha:
            # Duración de la función existente
            duracion_existente = 0
            for pelicula in peliculas_matriz[1:]:
                if pelicula[0] == funcion[1]:
                    duracion_existente = pelicula[3]
                    break
            if duracion_existente is None:
                continue

            inicio_existente = convertir_a_minutos(funcion[3])
            fin_existente = inicio_existente + duracion_existente
            # Chequear solapamiento
            if inicio_nuevo < fin_existente and fin_nuevo > inicio_existente:
                return True

    return False
#--------------------------------------------------
#Función para agregar función (Crud)
def agregarFuncion(funciones_matriz, peliculas_matriz, salas_matriz):
    print("Agregar Nueva Función:")
    nuevo_id = funciones_matriz[-1][0] + 1 if len(funciones_matriz) > 1 else 1
    pelicula_id = int(input("Ingrese ID de la Película: "))
    sala_id = int(input("Ingrese Número de Sala: "))
    horario = input("Ingrese Horario (HH:MM): ")
    fecha = input("Ingrese Fecha (YYYY-MM-DD): ")

    # Verificar si la película existe
    pelicula_existe = any(pelicula[0] == pelicula_id for pelicula in peliculas_matriz[1:])
    if not pelicula_existe:
        print(f"No existe ninguna película con ID {pelicula_id}. No se puede agregar la función.")
        return
    
    #Verificar si sala existe
    sala_existe = any(sala[0] == sala_id for sala in salas_matriz[1:])
    if not sala_existe:
        print(f"No existe ninguna sala con ID {sala_id}. No se puede agregar la función.")
        return
    
    if validar_horario_manual(horario) == False:
        print("El formato de horario es inválido. Use HH:MM en formato 24 horas.")
        return
    
    try:
        fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        print("Formato inválido. Debe ser YYYY-MM-DD. Volviendo al menú principal.")
        return

    
    if sala_ocupada_manual(sala_id, horario, fecha, pelicula_id, peliculas_matriz, funciones_matriz):
        print(f"La sala {sala_id} ya tiene una función programada que se superpone en ese horario.")
        return


    funciones_matriz.append([nuevo_id, pelicula_id, sala_id, horario, fecha])
    print(f"¡Función para la película ID {pelicula_id} en la sala {sala_id} agregada con éxito!")

#--------------------------------------------------
#Funcion para leer funciones (cRud)
def leerFuncionPorId(funciones_matriz):
    print("Consultar Función por ID:")
    id_buscar = int(input("Ingrese ID de la Función a Consultar: "))
    seEncontro = False
    for funcion in funciones_matriz[1:]:
        if funcion[0] == id_buscar:
            print(f"Función Encontrada: ID: {funcion[0]}, ID Película: {funcion[1]}, ID Sala: {funcion[2]}, Horario: {funcion[3]}, Fecha: {funcion[4]}")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ninguna función con ID {id_buscar}.")

def leerFuncionesPorFecha(funciones_matriz):
    print("Buscar Funciones por Fecha:")
    fecha_buscar = input("Ingrese la Fecha (YYYY-MM-DD) de las Funciones a Consultar: ")
    try:
        fecha_buscar = datetime.strptime(fecha_buscar, "%Y-%m-%d").date()
    except ValueError:
        print("Formato inválido. Debe ser YYYY-MM-DD. Volviendo al menú principal.")
        return
    funciones_encontradas = []
    for funcion in funciones_matriz[1:]:
        if funcion[4] == fecha_buscar:
            funciones_encontradas.append(funcion)
    if funciones_encontradas:
        print(f"Funciones Encontradas para la fecha {fecha_buscar}:")
        for funcion in funciones_encontradas:
            print(f"ID: {funcion[0]}, ID Película: {funcion[1]}, ID Sala: {funcion[2]}, Horario: {funcion[3]}, Fecha: {funcion[4]}")
    else:
        print(f"No se encontraron funciones para la fecha {fecha_buscar}.")
#--------------------------------------------------
#Funcion para actualizar función (crUd)
def actualizarFuncionPorId(funciones_matriz, peliculas_matriz, salas_matriz):
    print("Actualizar Función Existente por Id:")
    id_buscar = int(input("Ingrese ID de la Función a Actualizar: "))
    seEncontro = False
    for funcion in funciones_matriz[1:]:
        if funcion[0] == id_buscar:
            print(f"Función Encontrada: ID {funcion[0]}, ID Película: {funcion[1]}, ID Sala: {funcion[2]}, Horario: {funcion[3]}, Fecha: {funcion[4]}")
            nuevo_pelicula_id = input("Ingrese Nuevo ID de Película (dejar en blanco para no cambiar): ")
            nuevo_sala_id = input("Ingrese Nuevo Número de Sala (dejar en blanco para no cambiar): ")
            nuevo_horario = input("Ingrese Nuevo Horario (HH:MM) (dejar en blanco para no cambiar): ")
            nuevo_fecha = input("Ingrese Nueva Fecha (YYYY-MM-DD) (dejar en blanco para no cambiar): ")

            if nuevo_pelicula_id:
                nuevo_pelicula_id = int(nuevo_pelicula_id)
                # Verificar si la película existe
                pelicula_existe = any(pelicula[0] == nuevo_pelicula_id for pelicula in peliculas_matriz[1:])
                if not pelicula_existe:
                    print(f"No existe ninguna película con ID {nuevo_pelicula_id}. No se puede actualizar la función.")
                    return
                funcion[1] = nuevo_pelicula_id

            if nuevo_sala_id:
                nuevo_sala_id = int(nuevo_sala_id)
                # Verificar si sala existe
                sala_existe = any(sala[0] == nuevo_sala_id for sala in salas_matriz[1:])
                if not sala_existe:
                    print(f"No existe ninguna sala con ID {nuevo_sala_id}. No se puede actualizar la función.")
                    return
                funcion[2] = nuevo_sala_id

            if nuevo_horario:
                if validar_horario_manual(nuevo_horario) == False:
                    print("El formato de horario es inválido. Use HH:MM en formato 24 horas.")
                    return
                funcion[3] = nuevo_horario

            if nuevo_fecha:
                try:
                    nuevo_fecha_dt = datetime.strptime(nuevo_fecha, "%Y-%m-%d").date()
                    funcion[4] = nuevo_fecha_dt
                except ValueError:
                    print("Formato inválido. Debe ser YYYY-MM-DD. Volviendo al menú principal.")
                    return
            seEncontro = True
    if not seEncontro:
        print(f"No se encontró ninguna función con ID {id_buscar}.")
        return
    print(f"¡Función ID {id_buscar} actualizada con éxito!")

#--------------------------------------------------
#Funcion para eliminar función (cruD)
def eliminarFuncion(funciones_matriz):
    print("Eliminar Función Existente:")
    id_buscar = int(input("Ingrese ID de la Función a Eliminar: "))
    seEncontro = False
    for i, funcion in enumerate(funciones_matriz[1:], start=1):
        if funcion[0] == id_buscar:
            confirmacion = input(f"¿Está seguro que desea eliminar la función ID {id_buscar}? (s/n): ").lower()
            if confirmacion == 's':
                funciones_matriz.pop(i)
                print(f"¡Función ID {id_buscar} eliminada con éxito!")
            else:
                print("Eliminación cancelada.")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ninguna función con ID {id_buscar}.")
    

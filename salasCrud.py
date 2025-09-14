#--------------------------------------------------
# FUNCIONES CRUD PARA SALAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarSala(salas_lista):
    print("Agregar Nueva Sala:")
    nuevo_id = max([s['ID_Sala'] for s in salas_lista]) + 1 if salas_lista else 1
    nombre_sala = input("Ingrese Nombre de la Sala (ej: Sala 5): ")
    capacidad = int(input("Ingrese la Capacidad de la sala: "))
    tipo = input("Ingrese el Tipo de sala (ej: 2D, 3D, IMAX): ")
    
    nueva_sala = {
        'ID_Sala': nuevo_id,
        'Nombre_Sala': nombre_sala,
        'Capacidad': capacidad,
        'Tipo': tipo
    }
    salas_lista.append(nueva_sala)
    print(f"Sala '{nombre_sala}' agregada.")

def leerSalaPorId(salas_lista):
    print("Consultar Sala por ID:")
    id_buscar = int(input("Ingrese ID de la Sala a Consultar: "))
    
    sala_encontrada = None
    for s in salas_lista:
        if s['ID_Sala'] == id_buscar:
            sala_encontrada = s
            break
    
    if sala_encontrada:
        print(f"Sala Encontrada: ID: {sala_encontrada['ID_Sala']}, Nombre: {sala_encontrada['Nombre_Sala']}, Capacidad: {sala_encontrada['Capacidad']}, Tipo: {sala_encontrada['Tipo']}")
    else:
        print(f"No se encontró ninguna sala con ID {id_buscar}.")

def actualizarSala(salas_lista):
    print("Actualizar Sala Existente:")
    id_buscar = int(input("Ingrese ID de la Sala a Actualizar: "))
    
    sala_a_actualizar = None
    for s in salas_lista:
        if s['ID_Sala'] == id_buscar:
            sala_a_actualizar = s
            break

    if sala_a_actualizar:
        print(f"Sala Encontrada: {sala_a_actualizar['Nombre_Sala']}")
        nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ")
        nueva_capacidad = input("Ingrese Nueva Capacidad (dejar en blanco para no cambiar): ")
        nuevo_tipo = input("Ingrese Nuevo Tipo (dejar en blanco para no cambiar): ")
        
        if nuevo_nombre: sala_a_actualizar['Nombre_Sala'] = nuevo_nombre
        if nueva_capacidad: sala_a_actualizar['Capacidad'] = int(nueva_capacidad)
        if nuevo_tipo: sala_a_actualizar['Tipo'] = nuevo_tipo
            
        print(f"Sala ID {id_buscar} actualizada.")
    else:
        print(f"No se encontró ninguna sala con ID {id_buscar}.")

def eliminarSala(salas_lista, funciones_lista):
    print("Eliminar Sala Existente:")
    id_buscar = int(input("Ingrese ID de la Sala a Eliminar: "))
    
    sala_en_uso = False
    for funcion in funciones_lista:
        if funcion['ID_Sala'] == id_buscar:
            sala_en_uso = True
            break
    
    if sala_en_uso:
        print(f"La sala ID {id_buscar} está asignada a una o más funciones. No se puede eliminar.")
        return

    indice_a_eliminar = -1
    i = 0
    while i < len(salas_lista) and indice_a_eliminar == -1:
        if salas_lista[i]['ID_Sala'] == id_buscar:
            indice_a_eliminar = i
        i += 1

    if indice_a_eliminar != -1:
        sala = salas_lista[indice_a_eliminar]
        confirmacion = input(f"¿Está seguro que desea eliminar la sala '{sala['Nombre_Sala']}'? (s/n): ").lower()
        if confirmacion == 's':
            salas_lista.pop(indice_a_eliminar)
            print(f"Sala ID {id_buscar} eliminada.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ninguna sala con ID {id_buscar}.")
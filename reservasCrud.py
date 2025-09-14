from datetime import datetime
#--------------------------------------------------
# FUNCIONES CRUD PARA RESERVAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarReserva(reservas_lista, funciones_lista, clientes_lista):
    print("Agregar Nueva Reserva:")
    nuevo_id = max([r['ID_Reserva'] for r in reservas_lista]) + 1 if reservas_lista else 1001
    
    id_funcion = int(input("Ingrese ID de la Función: "))
    funcion_existe = False
    for f in funciones_lista:
        if f['ID_Funcion'] == id_funcion:
            funcion_existe = True
            break
    if not funcion_existe:
        print(f"No se encontró ninguna función con ID {id_funcion}.")
        return

    id_cliente = int(input("Ingrese ID del Cliente: "))
    cliente_existe = False
    for c in clientes_lista:
        if c['ID_Cliente'] == id_cliente:
            cliente_existe = True
            break
    if not cliente_existe:
        print(f"No se encontró ningún cliente con ID {id_cliente}.")
        return

    asientos = input("Ingrese los asientos a reservar (ej: F5, F6): ")
    
    nueva_reserva = {
        'ID_Reserva': nuevo_id,
        'ID_Funcion': id_funcion,
        'ID_Cliente': id_cliente,
        'Asientos': asientos,
        'Fecha_Reserva': datetime.now().date().isoformat()
    }
    reservas_lista.append(nueva_reserva)
    print(f"Reserva ID {nuevo_id} agregada.")

def leerReservaPorId(reservas_lista):
    print("Consultar Reserva por ID:")
    id_buscar = int(input("Ingrese ID de la Reserva a Consultar: "))
    
    reserva_encontrada = None
    for r in reservas_lista:
        if r['ID_Reserva'] == id_buscar:
            reserva_encontrada = r
            break
    
    if reserva_encontrada:
        print(f"Reserva Encontrada: ID: {reserva_encontrada['ID_Reserva']}, ID_Funcion: {reserva_encontrada['ID_Funcion']}, ID_Cliente: {reserva_encontrada['ID_Cliente']}, Asientos: {reserva_encontrada['Asientos']}, Fecha_Reserva: {reserva_encontrada['Fecha_Reserva']}")
    else:
        print(f"No se encontró ninguna reserva con ID {id_buscar}.")

def actualizarReserva(reservas_lista, funciones_lista, clientes_lista):
    print("Actualizar Reserva Existente:")
    id_buscar = int(input("Ingrese ID de la Reserva a Actualizar: "))
    
    reserva_a_actualizar = None
    for r in reservas_lista:
        if r['ID_Reserva'] == id_buscar:
            reserva_a_actualizar = r
            break
    
    if reserva_a_actualizar:
        print(f"Reserva Encontrada: ID_Funcion: {reserva_a_actualizar['ID_Funcion']}, ID_Cliente: {reserva_a_actualizar['ID_Cliente']}, Asientos: {reserva_a_actualizar['Asientos']}")
        
        nuevo_id_funcion_str = input("Ingrese Nuevo ID de Función (dejar en blanco para no cambiar): ")
        if nuevo_id_funcion_str:
            nuevo_id_funcion = int(nuevo_id_funcion_str)
            funcion_existe = False
            for f in funciones_lista:
                if f['ID_Funcion'] == nuevo_id_funcion:
                    funcion_existe = True
                    break
            if not funcion_existe:
                print(f"No se encontró ninguna función con ID {nuevo_id_funcion}.")
                return
            reserva_a_actualizar['ID_Funcion'] = nuevo_id_funcion

        nuevo_id_cliente_str = input("Ingrese Nuevo ID de Cliente (dejar en blanco para no cambiar): ")
        if nuevo_id_cliente_str:
            nuevo_id_cliente = int(nuevo_id_cliente_str)
            cliente_existe = False
            for c in clientes_lista:
                if c['ID_Cliente'] == nuevo_id_cliente:
                    cliente_existe = True
                    break
            if not cliente_existe:
                print(f"No se encontró ningún cliente con ID {nuevo_id_cliente}.")
                return
            reserva_a_actualizar['ID_Cliente'] = nuevo_id_cliente

        nuevos_asientos = input("Ingrese Nuevos Asientos (dejar en blanco para no cambiar): ")
        if nuevos_asientos:
            reserva_a_actualizar['Asientos'] = nuevos_asientos
        
        reserva_a_actualizar['Fecha_Reserva'] = datetime.now().date().isoformat()
        print(f"Reserva ID {id_buscar} actualizada.")
    else:
        print(f"No se encontró ninguna reserva con ID {id_buscar}.")

def eliminarReserva(reservas_lista):
    print("Eliminar Reserva Existente:")
    id_buscar = int(input("Ingrese ID de la Reserva a Eliminar: "))
    
    indice_a_eliminar = -1
    i = 0
    while i < len(reservas_lista) and indice_a_eliminar == -1:
        if reservas_lista[i]['ID_Reserva'] == id_buscar:
            indice_a_eliminar = i
        i += 1
            
    if indice_a_eliminar != -1:
        confirmacion = input(f"¿Está seguro que desea eliminar la reserva ID {id_buscar}? (s/n): ").lower()
        if confirmacion == 's':
            reservas_lista.pop(indice_a_eliminar)
            print(f"Reserva ID {id_buscar} eliminada.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ninguna reserva con ID {id_buscar}.")
from datetime import datetime
import re
#--------------------------------------------------
# FUNCIONES CRUD PARA RESERVAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarReserva(reservas_lista, funciones_lista, clientes_lista):
    print("Agregar Nueva Reserva:")
    nuevo_id = max([r['ID_Reserva'] for r in reservas_lista]) + 1 if reservas_lista else 1001

    # --- Validar ID de función ---
    try:
        id_funcion = int(input("Ingrese ID de la Función: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    funcion_existe = False
    for f in funciones_lista:
        if f['ID_Funcion'] == id_funcion:
            funcion_existe = True
            break
    if not funcion_existe:
        print(f"No se encontró ninguna función con ID {id_funcion}.")
        return

    # --- Validar ID de cliente ---
    try:
        id_cliente = int(input("Ingrese ID del Cliente: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    cliente_existe = False
    for c in clientes_lista:
        if c['ID_Cliente'] == id_cliente:
            cliente_existe = True
            break
    if not cliente_existe:
        print(f"No se encontró ningún cliente con ID {id_cliente}.")
        return

    # --- Validar formato de asientos ---
    asientos_input = input("Ingrese los asientos a reservar (ej: F5, F6): ").replace(" ", "")
    asientos = asientos_input.split(",")

    patron_asiento = r'^[A-Z][0-9]+$'
    for asiento in asientos:
        if not re.match(patron_asiento, asiento):
            print(f"Error: El formato del asiento '{asiento}' no es válido. Use formato Letra+Número (ej: F5).")
            return

    # --- Validar si los asientos ya están reservados para esa función ---
    asientos_ocupados = set()
    for reserva in reservas_lista:
        if reserva['ID_Funcion'] == id_funcion:
            reservados_previos = reserva['Asientos'].replace(" ", "").split(",")
            for a in reservados_previos:
                asientos_ocupados.add(a.upper())

    asientos_conflictivos = []
    for a in asientos:
        if a.upper() in asientos_ocupados:
            asientos_conflictivos.append(a)

    if len(asientos_conflictivos) > 0:
        print(f"Error: Los asientos {', '.join(asientos_conflictivos)} ya están reservados para esta función.")
        return

    # --- Si todo está correcto, registrar la reserva ---
    nueva_reserva = {
        'ID_Reserva': nuevo_id,
        'ID_Funcion': id_funcion,
        'ID_Cliente': id_cliente,
        'Asientos': ", ".join(asientos),
        'Fecha_Reserva': datetime.now().date().isoformat()
    }

    reservas_lista.append(nueva_reserva)
    print(f"Reserva ID {nuevo_id} agregada correctamente.")


def leerReservaPorId(reservas_lista):
    print("Consultar Reserva por ID:")
    try:
        id_buscar = int(input("Ingrese ID de la Reserva a Consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
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
    try:
        id_buscar = int(input("Ingrese ID de la Reserva a Actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    reserva_a_actualizar = None
    for r in reservas_lista:
        if r['ID_Reserva'] == id_buscar:
            reserva_a_actualizar = r
            break
    
    if reserva_a_actualizar:
        print(f"Reserva Encontrada: ID_Funcion: {reserva_a_actualizar['ID_Funcion']}, ID_Cliente: {reserva_a_actualizar['ID_Cliente']}, Asientos: {reserva_a_actualizar['Asientos']}")
        
        nuevo_id_funcion_str = input("Ingrese Nuevo ID de Función (dejar en blanco para no cambiar): ")
        if nuevo_id_funcion_str:
            try:
                nuevo_id_funcion = int(nuevo_id_funcion_str)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
                return
            funcion_existe = False
            for f in funciones_lista:
                if f['ID_Funcion'] == nuevo_id_funcion:
                    funcion_existe = True
                    break
            if not funcion_existe:
                print(f"No se encontró ninguna función con ID {nuevo_id_funcion}.")
                return
            reserva_a_actualizar['ID_Funcion'] = nuevo_id_funcion

        try:
            nuevo_id_cliente_str = input("Ingrese Nuevo ID de Cliente (dejar en blanco para no cambiar): ")
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return
        if nuevo_id_cliente_str:
            nuevo_id_cliente = nuevo_id_cliente_str
            cliente_existe = False
            for c in clientes_lista:
                if c['ID_Cliente'] == nuevo_id_cliente:
                    cliente_existe = True
                    break
            if not cliente_existe:
                print(f"No se encontró ningún cliente con ID {nuevo_id_cliente}.")
                return
            reserva_a_actualizar['ID_Cliente'] = nuevo_id_cliente

        asientos_input = input("Ingrese Nuevos Asientos (F5,F6) (dejar en blanco para no cambiar): ").replace(" ", "")
        asientos = asientos_input.split(",")
    
        if asientos:
            patron_asiento = r'^[A-Z][0-9]+$'
            for asiento in asientos:
                if not re.match(patron_asiento, asiento):
                    print(f"Error: El formato del asiento '{asiento}' no es válido. Use formato Letra+Número (ej: F5).")
                    return

            # --- Validar si los asientos ya están reservados para esa función ---
            asientos_ocupados = set()
            for reserva in reservas_lista:
                if reserva['ID_Funcion'] == id_buscar:
                    reservados_previos = reserva['Asientos'].replace(" ", "").split(",")
                    for a in reservados_previos:
                        asientos_ocupados.add(a.upper())

            asientos_conflictivos = []
            for a in asientos:
                if a.upper() in asientos_ocupados:
                    asientos_conflictivos.append(a)

            if len(asientos_conflictivos) > 0:
                print(f"Error: Los asientos {', '.join(asientos_conflictivos)} ya están reservados para esta función.")
                return
            reserva_a_actualizar['Asientos'] = asientos_input
        
        reserva_a_actualizar['Fecha_Reserva'] = datetime.now().date().isoformat()
        print(f"Reserva ID {id_buscar} actualizada.")
    else:
        print(f"No se encontró ninguna reserva con ID {id_buscar}.")

def eliminarReserva(reservas_lista):
    print("Eliminar Reserva Existente:")
    try:
        id_buscar = int(input("Ingrese ID de la Reserva a Eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
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
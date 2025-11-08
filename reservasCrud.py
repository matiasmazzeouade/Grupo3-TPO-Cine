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

    # --- Validación estricta del formato de asientos ---
    asientos = [a.upper() for a in asientos]  # normalizar

    patron_asiento = r'^[A-Z][1-9][0-9]{0,2}$'  # Letra + número entre 1 y 999 (sin 0 adelante)

    # Ver duplicados dentro de la misma reserva
    duplicados = {a for a in asientos if asientos.count(a) > 1}
    if duplicados:
        print(f"Error: Los asientos {', '.join(duplicados)} están repetidos dentro de la misma reserva.")
        return

    # Validar formato general
    for asiento in asientos:
        if not re.match(patron_asiento, asiento):
            print(f"Error: El asiento '{asiento}' no es válido. Use formato Letra+Número (ej: F5).")
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

    # Buscar reserva
    reserva_a_actualizar = next((r for r in reservas_lista if r['ID_Reserva'] == id_buscar), None)

    if not reserva_a_actualizar:
        print(f"No se encontró ninguna reserva con ID {id_buscar}.")
        return

    print(f"Reserva Encontrada: ID_Funcion: {reserva_a_actualizar['ID_Funcion']}, "
          f"ID_Cliente: {reserva_a_actualizar['ID_Cliente']}, "
          f"Asientos: {reserva_a_actualizar['Asientos']}")

    # --- Actualizar ID_Funcion ---
    nuevo_id_funcion_str = input("Ingrese Nuevo ID de Función (dejar en blanco para no cambiar): ").strip()
    if nuevo_id_funcion_str:
        try:
            nuevo_id_funcion = int(nuevo_id_funcion_str)
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return

        # Validar existencia
        if not any(f['ID_Funcion'] == nuevo_id_funcion for f in funciones_lista):
            print(f"No se encontró ninguna función con ID {nuevo_id_funcion}.")
            return

        reserva_a_actualizar['ID_Funcion'] = nuevo_id_funcion

    funcion_actual = reserva_a_actualizar['ID_Funcion']

    # --- Actualizar ID_Cliente ---
    nuevo_id_cliente_str = input("Ingrese Nuevo ID de Cliente (dejar en blanco para no cambiar): ").strip()
    if nuevo_id_cliente_str:
        try:
            nuevo_id_cliente = int(nuevo_id_cliente_str)
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return

        if not any(c['ID_Cliente'] == nuevo_id_cliente for c in clientes_lista):
            print(f"No se encontró ningún cliente con ID {nuevo_id_cliente}.")
            return

        reserva_a_actualizar['ID_Cliente'] = nuevo_id_cliente

    # --- Actualizar Asientos ---
    asientos_input = input("Ingrese Nuevos Asientos (F5,F6) (dejar en blanco para no cambiar): ").strip()

    if asientos_input:
        asientos_input = asientos_input.replace(" ", "")
        asientos = [a.upper() for a in asientos_input.split(",")]
        
        # --- Validación estricta del formato de asientos ---
        patron_asiento = r'^[A-Z][1-9][0-9]{0,2}$'  # Letra + número 1–999
        
        # Ver duplicados dentro de la misma reserva
        duplicados = {a for a in asientos if asientos.count(a) > 1}
        if duplicados:
            print(f"Error: Los asientos {', '.join(duplicados)} están repetidos dentro de la misma reserva.")
            return
        
        # Validar formato general
        for asiento in asientos:
            if not re.match(patron_asiento, asiento):
                print(f"Error: El asiento '{asiento}' no es válido. Use formato Letra+Número (ej: F5).")
                return
        
        
        # Obtener asientos ocupados EXCLUYENDO esta reserva
        asientos_ocupados = set()
        for r in reservas_lista:
            if r['ID_Funcion'] == funcion_actual and r['ID_Reserva'] != id_buscar:
                prev = r['Asientos'].replace(" ", "").upper().split(",")
                asientos_ocupados.update(prev)

        # Validar conflictos reales
        conflictivos = [a for a in asientos if a in asientos_ocupados]

        if conflictivos:
            print(f"Error: Los asientos {', '.join(conflictivos)} ya están reservados para esta función.")
            return

        # Actualizar asientos
        reserva_a_actualizar['Asientos'] = ", ".join(asientos)

    # Actualizar fecha
    reserva_a_actualizar['Fecha_Reserva'] = datetime.now().date().isoformat()

    print(f"Reserva ID {id_buscar} actualizada correctamente.")

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

def menu_reservas(reservas_lista, funciones_lista, clientes_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Reservas ---")
        print("1. Agregar reserva")
        print("2. Consultar por ID")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("x. Volver")

        op = input("Seleccione opción: ").lower()

        if op == "1":
            agregarReserva(reservas_lista, funciones_lista, clientes_lista)

        elif op == "2":
            leerReservaPorId(reservas_lista)

        elif op == "3":
            actualizarReserva(reservas_lista, funciones_lista, clientes_lista)

        elif op == "4":
            eliminarReserva(reservas_lista)

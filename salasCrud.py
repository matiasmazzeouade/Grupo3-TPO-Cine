import re
#--------------------------------------------------
# FUNCIONES CRUD PARA SALAS (CON DICCIONARIOS)
#--------------------------------------------------

def agregarSala(salas_lista):
    print("Agregar Nueva Sala:")
    nuevo_id = max([s['ID_Sala'] for s in salas_lista]) + 1 if salas_lista else 1

    # --- Validar nombre ---
    nombre_sala = input("Ingrese Nombre de la Sala (ej: Sala 5): ").strip()
    if not nombre_sala or len(nombre_sala) < 2:
        print("Error: El nombre de la sala no puede estar vacío y debe tener al menos 2 caracteres.")
        return

    # --- Validar capacidad ---
    try:
        capacidad = int(input("Ingrese la Capacidad de la sala: "))
        if capacidad <= 0:
            print("Error: La capacidad debe ser un entero positivo.")
            return
    except ValueError:
        print("Error: La capacidad debe ser un número entero.")
        return

    # --- Validar tipo ---
    tipo = input("Ingrese el Tipo de sala (ej: 2D, 3D, IMAX): ").strip().upper()
    if not tipo:
        print("Error: El tipo de sala no puede estar vacío.")
        return

    # Reglas opcionales de formato
    patron_tipo = r'^[A-Z0-9]{2,6}$'  # 2D, 3D, IMAX, XD, VIP, etc.
    if not re.match(patron_tipo, tipo):
        print("Error: El tipo de sala debe ser corto y alfanumérico (ej: 2D, 3D, IMAX, XD).")
        return

    nueva_sala = {
        'ID_Sala': nuevo_id,
        'Nombre_Sala': nombre_sala,
        'Capacidad': capacidad,
        'Tipo': tipo
    }
    salas_lista.append(nueva_sala)
    print(f"Sala '{nombre_sala}' agregada correctamente.")

def leerSalaPorId(salas_lista):
    print("Consultar Sala por ID:")
    try:
        id_buscar = int(input("Ingrese ID de la Sala a Consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
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
    try:   
        id_buscar = int(input("Ingrese ID de la Sala a Actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    sala_a_actualizar = None
    for s in salas_lista:
        if s['ID_Sala'] == id_buscar:
            sala_a_actualizar = s
            break

    if not sala_a_actualizar:
        print(f"No se encontró ninguna sala con ID {id_buscar}.")
        return

    print(f"Sala Encontrada: {sala_a_actualizar['Nombre_Sala']}")

    nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ").strip()
    nueva_capacidad_str = input("Ingrese Nueva Capacidad (dejar en blanco para no cambiar): ").strip()
    nuevo_tipo = input("Ingrese Nuevo Tipo (dejar en blanco para no cambiar): ").strip().upper()

    # --- Validar y actualizar nombre ---
    if nuevo_nombre:
        if len(nuevo_nombre) < 2:
            print("Error: El nombre debe tener al menos 2 caracteres.")
            return
        sala_a_actualizar['Nombre_Sala'] = nuevo_nombre

    # --- Validar y actualizar capacidad ---
    if nueva_capacidad_str:
        try:
            nueva_capacidad = int(nueva_capacidad_str)
            if nueva_capacidad <= 0:
                print("Error: La capacidad debe ser un entero positivo. No se actualizó la capacidad.")
            else:
                sala_a_actualizar['Capacidad'] = nueva_capacidad
        except ValueError:
            print("Error: La capacidad debe ser un número entero.")
            return

    # --- Validar y actualizar tipo ---
    if nuevo_tipo:
        patron_tipo = r'^[A-Z0-9]{2,6}$'
        if not re.match(patron_tipo, nuevo_tipo):
            print("Error: El tipo debe ser corto y alfanumérico (ej: 2D, 3D, IMAX, XD).")
            return
        sala_a_actualizar['Tipo'] = nuevo_tipo

    print(f"Sala ID {id_buscar} actualizada correctamente.")

def eliminarSala(salas_lista, funciones_lista, reservas_lista):
    print("Eliminar Sala:")
    try:
        id_buscar = int(input("ID de sala: "))
    except ValueError:
        print("ID inválido.")
        return

    # Buscar sala
    sala = next((s for s in salas_lista if s['ID_Sala'] == id_buscar), None)
    if not sala:
        print("Sala no encontrada.")
        return

    # Buscar funciones asociadas
    funciones_asociadas = [f['ID_Funcion'] for f in funciones_lista if f['ID_Sala'] == id_buscar]

    # Si tiene funciones → NO SE PUEDE ELIMINAR
    if funciones_asociadas:
        print("La sala tiene funciones asignadas y no se puede eliminar.")
        return

    # Si no tiene funciones → pedir confirmación
    confirm = input("¿Eliminar sala? (s/n): ").lower()
    if confirm != "s":
        print("Cancelado.")
        return

    # Eliminar sala
    salas_lista.remove(sala)

    print("Sala eliminada correctamente.")


def menu_salas(salas_lista, funciones_lista, reservas_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Salas ---")
        print("1. Agregar")
        print("2. Consultar por ID")
        print("3. Actualizar")
        print("4. Eliminar (cascada)")
        print("x. Volver")

        op = input("Seleccione: ").lower()

        if op == "1":
            agregarSala(salas_lista)

        elif op == "2":
            leerSalaPorId(salas_lista)

        elif op == "3":
            actualizarSala(salas_lista)

        elif op == "4":
            eliminarSala(salas_lista, funciones_lista, reservas_lista)

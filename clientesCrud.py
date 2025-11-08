import re

#--------------------------------------------------
# FUNCIONES CRUD PARA CLIENTES (CON DICCIONARIOS)
#--------------------------------------------------

def agregarCliente(clientes_lista):
    print("Agregar Nuevo Cliente:")
    
    nuevo_id = max([c['ID_Cliente'] for c in clientes_lista]) + 1 if clientes_lista else 101

    nombre = input("Ingrese Nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    apellido = input("Ingrese Apellido: ").strip()
    if not apellido:
        print("Error: El apellido no puede estar vacío.")
        return

    # --- Validar Email ---
    email = input("Ingrese Email: ").strip()
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(patron_email, email):
        print("Error: El formato del email no es válido.")
        return

    # Validar duplicado
    if any(c['Email'].lower() == email.lower() for c in clientes_lista):
        print("Error: Ya existe un cliente registrado con ese email.")
        return

    # --- Validar Edad ---
    try:
        edad = int(input("Ingrese Edad: "))
        if edad <= 0 or edad > 120:
            print("Error: La edad debe estar entre 1 y 120 años.")
            return
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    # --- Validar Teléfono ---
    telefono = input("Ingrese Teléfono: ").strip()
    patron_tel = r'^\d+$'
    if not re.match(patron_tel, telefono):
        print("Error: El teléfono debe contener solo números.")
        return

    nuevo_cliente = {
        'ID_Cliente': nuevo_id,
        'Nombre': nombre,
        'Apellido': apellido,
        'Email': email,
        'Edad': edad,
        'Telefono': telefono
    }

    clientes_lista.append(nuevo_cliente)
    print(f"Cliente '{nombre} {apellido}' agregado correctamente.")

# FUNCIÓN RECURSIVA
def _buscar_cliente_recursiva(lista, id_buscar):
    """
    Función auxiliar recursiva para buscar un cliente por ID.
    """
    if not lista:
        return None
    
    if lista[0]['ID_Cliente'] == id_buscar:
        return lista[0]
    
    return _buscar_cliente_recursiva(lista[1:], id_buscar)

def leerClientePorId(clientes_lista):
    print("Consultar cliente por ID:")
    try:
        id_buscar = int(input("Ingrese ID del cliente a consultar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    cliente_encontrado = _buscar_cliente_recursiva(clientes_lista, id_buscar)
            
    if cliente_encontrado:
        print(f"Cliente Encontrado: ID: {cliente_encontrado['ID_Cliente']}, Nombre: {cliente_encontrado['Nombre']}, Apellido: {cliente_encontrado['Apellido']}, Email: {cliente_encontrado['Email']}, Teléfono: {cliente_encontrado['Telefono']}")
    else:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")

def leerClientePorNombre(clientes_lista):
    print("Buscar Cliente por Nombre y/o Apellido:")
    nombre_buscar = input("Ingrese el Nombre o parte del Nombre (dejar en blanco para omitir): ").lower()
    apellido_buscar = input("Ingrese el Apellido o parte del Apellido (dejar en blanco para omitir): ").lower()
    
    clientes_encontrados = [
        c for c in clientes_lista 
        if (not nombre_buscar or nombre_buscar in c['Nombre'].lower()) and 
           (not apellido_buscar or apellido_buscar in c['Apellido'].lower())
    ]
    
    if clientes_encontrados:
        print("Clientes Encontrados:")
        for cliente in clientes_encontrados:
            print(f"ID: {cliente['ID_Cliente']}, Nombre: {cliente['Nombre']}, Apellido: {cliente['Apellido']}, Email: {cliente['Email']}, Teléfono: {cliente['Telefono']}")
    else:
        print("No se encontraron clientes que coincidan con la búsqueda.")

def actualizarClientePorId(clientes_lista):
    print("Actualizar Cliente Existente por ID:")
    try:
        id_buscar = int(input("Ingrese ID del Cliente a Actualizar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    # Buscar cliente
    cliente_a_actualizar = _buscar_cliente_recursiva(clientes_lista, id_buscar)

    if cliente_a_actualizar:
        print(f"Cliente Encontrado: {cliente_a_actualizar['Nombre']} {cliente_a_actualizar['Apellido']}")

        nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ").strip()
        nuevo_apellido = input("Ingrese Nuevo Apellido (dejar en blanco para no cambiar): ").strip()
        nuevo_email = input("Ingrese Nuevo Email (dejar en blanco para no cambiar): ").strip()
        nuevo_telefono = input("Ingrese Nuevo Teléfono (dejar en blanco para no cambiar): ").strip()
        nuevo_edad_str = input("Ingrese Nueva Edad (dejar en blanco para no cambiar): ").strip()

        # --- Actualizar Nombre ---
        if nuevo_nombre:
            cliente_a_actualizar['Nombre'] = nuevo_nombre

        # --- Actualizar Apellido ---
        if nuevo_apellido:
            cliente_a_actualizar['Apellido'] = nuevo_apellido

        # --- Validar y actualizar Email ---
        if nuevo_email:
            patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(patron_email, nuevo_email):
                print("Error: El formato del email no es válido.")
                return

            # Verificar que no haya otro cliente con ese email
            if any(c['Email'].lower() == nuevo_email.lower() and c['ID_Cliente'] != cliente_a_actualizar['ID_Cliente']
                   for c in clientes_lista):
                print("Error: Ya existe otro cliente con ese email.")
                return

            cliente_a_actualizar['Email'] = nuevo_email

        # --- Validar y actualizar Teléfono ---
        if nuevo_telefono:
            patron_tel = r'^\d+$'
            if not re.match(patron_tel, nuevo_telefono):
                print("Error: El teléfono debe contener solo números.")
                return
            cliente_a_actualizar['Telefono'] = nuevo_telefono

        # --- Validar y actualizar Edad ---
        if nuevo_edad_str:
            try:
                nueva_edad = int(nuevo_edad_str)
                if nueva_edad <= 0 or nueva_edad > 120:
                    print("Error: La edad debe estar entre 1 y 120 años.")
                    return
                cliente_a_actualizar['Edad'] = nueva_edad
            except ValueError:
                print("Error: La edad debe ser un número entero.")
                return

        print(f"Cliente ID {id_buscar} actualizado correctamente.")

    else:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")

def eliminarCliente(clientes_lista, reservas_lista):
    print("Eliminar Cliente:")
    try:
        id_buscar = int(input("Ingrese ID del Cliente: "))
    except ValueError:
        print("Debe ser un número entero.")
        return

    cliente = _buscar_cliente_recursiva(clientes_lista, id_buscar)

    if not cliente:
        print("Cliente no encontrado.")
        return

    confirm = input(f"¿Eliminar cliente y TODAS sus reservas? (s/n): ").lower()
    if confirm != "s":
        print("Cancelado.")
        return

    reservas_lista[:] = [r for r in reservas_lista if r['ID_Cliente'] != id_buscar]

    clientes_lista.remove(cliente)

    print("Cliente eliminado junto con sus reservas.")

def leerUltimosDosClientes(clientes_lista):
    if len(clientes_lista)<2:
         raise ValueError("No hay suficientes clientes para mostrar.")
    print("Últimos Dos Clientes Agregados:")
    ultimos_dos = clientes_lista[-2:]
    for cliente in ultimos_dos:
        print(f"ID: {cliente['ID_Cliente']}, Nombre: {cliente['Nombre']}, Apellido: {cliente['Apellido']}, Email: {cliente['Email']}, Teléfono: {cliente['Telefono']}")

def menu_clientes(clientes_lista, reservas_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Clientes ---")
        print("1. Agregar")
        print("2. Consultar por ID")
        print("3. Consultar por nombre")
        print("4. Actualizar")
        print("5. Eliminar (cascada)")
        print("6. Últimos 2 clientes")
        print("x. Volver")

        op = input("Seleccione: ").lower()

        if op == "1":
            agregarCliente(clientes_lista)

        elif op == "2":
            leerClientePorId(clientes_lista)

        elif op == "3":
            leerClientePorNombre(clientes_lista)

        elif op == "4":
            actualizarClientePorId(clientes_lista)

        elif op == "5":
            eliminarCliente(clientes_lista, reservas_lista)

        elif op == "6":
            leerUltimosDosClientes(clientes_lista)

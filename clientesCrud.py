import re

#--------------------------------------------------
# FUNCIONES CRUD PARA CLIENTES (CON DICCIONARIOS)
#--------------------------------------------------

def agregarCliente(clientes_lista):
    print("Agregar Nuevo Cliente:")
    nuevo_id = max([c['ID_Cliente'] for c in clientes_lista]) + 1 if clientes_lista else 101
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    
    # --- EXPRESIONES REGULARES ---
    while True:
        email = input("Ingrese Email (ej: usuario@dominio.com): ")
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron_email, email):
            break 
        else:
            print("Error: El formato del email no es válido. Inténtelo de nuevo.")
    
    while True:
        telefono = input("Ingrese Teléfono (solo números, ej: 1122334455): ")
        patron_telefono = r'^\d+$'
        if re.match(patron_telefono, telefono):
            break 
        else:
            print("Error: El teléfono debe contener solo números. Inténtelo de nuevo.")
    try:       
        edad = int(input("Ingrese Edad: "))
        if edad < 0:
            print("Error: La edad no puede ser negativa. Volviendo al menú principal.")
            return
    except ValueError:
        print("Error: La edad debe ser un número entero. Volviendo al menú principal.")
        return
    
    nuevo_cliente = {
        'ID_Cliente': nuevo_id,
        'Nombre': nombre,
        'Apellido': apellido,
        'Email': email,
        'Telefono': telefono,
        'Edad': edad
    }
    clientes_lista.append(nuevo_cliente)
    print(f"Cliente '{nombre} {apellido}' agregado.")

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
    
    cliente_a_actualizar = _buscar_cliente_recursiva(clientes_lista, id_buscar)

    if cliente_a_actualizar:
        print(f"Cliente Encontrado: {cliente_a_actualizar['Nombre']} {cliente_a_actualizar['Apellido']}")
        nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ")
        nuevo_apellido = input("Ingrese Nuevo Apellido (dejar en blanco para no cambiar): ")
        nuevo_email = input("Ingrese Nuevo Email (dejar en blanco para no cambiar): ")
        nuevo_telefono = input("Ingrese Nuevo Teléfono (dejar en blanco para no cambiar): ")
        
        if nuevo_nombre: cliente_a_actualizar['Nombre'] = nuevo_nombre
        if nuevo_apellido: cliente_a_actualizar['Apellido'] = nuevo_apellido
        if nuevo_email: cliente_a_actualizar['Email'] = nuevo_email
        if nuevo_telefono: cliente_a_actualizar['Telefono'] = nuevo_telefono
        
        print(f"Cliente ID {id_buscar} actualizado.")
    else:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")

def eliminarCliente(clientes_lista):
    print("Eliminar Cliente Existente:")
    try:
        id_buscar = int(input("Ingrese ID del Cliente a Eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
        
    cliente_a_eliminar = _buscar_cliente_recursiva(clientes_lista, id_buscar)
            
    if cliente_a_eliminar:
        confirmacion = input(f"¿Está seguro que desea eliminar al cliente '{cliente_a_eliminar['Nombre']} {cliente_a_eliminar['Apellido']}'? (s/n): ").lower()
        if confirmacion == 's':
            clientes_lista.remove(cliente_a_eliminar)
            print(f"Cliente ID {id_buscar} eliminado.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")

def leerUltimosDosClientes(clientes_lista):
    if len(clientes_lista)<2:
         raise ValueError("No hay suficientes clientes para mostrar.")
    print("Últimos Dos Clientes Agregados:")
    ultimos_dos = clientes_lista[-2:]
    for cliente in ultimos_dos:
        print(f"ID: {cliente['ID_Cliente']}, Nombre: {cliente['Nombre']}, Apellido: {cliente['Apellido']}, Email: {cliente['Email']}, Teléfono: {cliente['Telefono']}")
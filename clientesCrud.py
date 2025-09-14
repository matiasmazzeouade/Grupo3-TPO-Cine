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
            
    edad = int(input("Ingrese Edad: "))
    
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

def leerClientePorId(clientes_lista):
    print("Consultar cliente por ID:")
    id_buscar = int(input("Ingrese ID del cliente a consultar: "))
    
    cliente_encontrado = ""
    i = 0
    while i < len(clientes_lista) and cliente_encontrado is "":
        if clientes_lista[i]['ID_Cliente'] == id_buscar:
            cliente_encontrado = clientes_lista[i]
        i += 1
            
    if cliente_encontrado != "":
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
    id_buscar = int(input("Ingrese ID del Cliente a Actualizar: "))
    
    cliente_a_actualizar = None
    i = 0
    while i < len(clientes_lista) and cliente_a_actualizar is None:
        if clientes_lista[i]['ID_Cliente'] == id_buscar:
            cliente_a_actualizar = clientes_lista[i]
        i += 1

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
    id_buscar = int(input("Ingrese ID del Cliente a Eliminar: "))
    
    indice_a_eliminar = -1
    i = 0
    while i < len(clientes_lista) and indice_a_eliminar == -1:
        if clientes_lista[i]['ID_Cliente'] == id_buscar:
            indice_a_eliminar = i
        i += 1
            
    if indice_a_eliminar != -1:
        cliente = clientes_lista[indice_a_eliminar]
        confirmacion = input(f"¿Está seguro que desea eliminar al cliente '{cliente['Nombre']} {cliente['Apellido']}'? (s/n): ").lower()
        if confirmacion == 's':
            clientes_lista.pop(indice_a_eliminar)
            print(f"Cliente ID {id_buscar} eliminado.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")
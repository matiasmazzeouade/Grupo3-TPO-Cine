#--------------------------------------------------
# FUNCIONES CRUD PARA CLIENTES
#--------------------------------------------------
#Funcion para agregar cliente (Crud)
def agregarCliente(clientes_matriz):
    print("Agregar Nuevo Cliente:")
    nuevo_id = clientes_matriz[-1][0] + 1 if len(clientes_matriz) > 1 else 1
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    email = input("Ingrese Email: ")
    telefono = input("Ingrese Teléfono: ")
    clientes_matriz.append([nuevo_id, nombre, apellido, email, telefono])
    print(f"¡Cliente '{nombre} {apellido}' agregado con éxito!")

#--------------------------------------------------
#Funcion para leer clientes (cRud)
def leerClientePorId(clientes_matriz):
    print("Consultar Cliente por ID:")
    id_buscar = int(input("Ingrese ID del Cliente a Consultar: "))
    clientes_encontrados = []
    for cliente in clientes_matriz[1:]:
        if cliente[0] == id_buscar:
            clientes_encontrados.append(cliente)
    if clientes_encontrados:
        for cliente in clientes_encontrados:
            print(f"Cliente Encontrado: ID: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Email: {cliente[3]}, Teléfono: {cliente[4]}")

def leerClientePorNombre(clientes_matriz):
    print("Buscar Cliente por Nombre y/o:")
    nombre_buscar = input("Ingrese el Nombre o parte del Nombre del Cliente (dejar en blanco para omitir): ").lower()
    apellido_buscar = input("Ingrese el Apellido o parte del Apellido del Cliente (dejar en blanco para omitir): ").lower()
    clientes_encontrados = []
    for cliente in clientes_matriz[1:]:
        if (not nombre_buscar or nombre_buscar in cliente[1].lower()) and (not apellido_buscar or apellido_buscar in cliente[2].lower() and (nombre_buscar or apellido_buscar)):
            clientes_encontrados.append(cliente)
    if clientes_encontrados:
        print("Clientes Encontrados:")
        for cliente in clientes_encontrados:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Apellido: {cliente[2]}, Email: {cliente[3]}, Teléfono: {cliente[4]}")
    else:
        print(f"No se encontraron clientes que coincidan con '{nombre_buscar}'.")

#--------------------------------------------------
#Funcion para actualizar cliente (crUd)

def actualizarClientePorId(clientes_matriz):
    print("Actualizar Cliente Existente por Id:")
    id_buscar = int(input("Ingrese ID del Cliente a Actualizar: "))
    seEncontro = False
    for cliente in clientes_matriz[1:]:
        if cliente[0] == id_buscar:
            print(f"Cliente Encontrado: {cliente[1]} {cliente[2]}")
            nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ")
            nuevo_apellido = input("Ingrese Nuevo Apellido (dejar en blanco para no cambiar): ")
            nuevo_email = input("Ingrese Nuevo Email (dejar en blanco para no cambiar): ")
            nuevo_telefono = input("Ingrese Nuevo Teléfono (dejar en blanco para no cambiar): ")

            if nuevo_nombre:
                cliente[1] = nuevo_nombre
            if nuevo_apellido:
                cliente[2] = nuevo_apellido
            if nuevo_email:
                cliente[3] = nuevo_email
            if nuevo_telefono:
                cliente[4] = nuevo_telefono

            print(f"¡Cliente ID {id_buscar} actualizado con éxito!")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")

def actualizarClientePorNombre(clientes_matriz):
    print("Actualizar Cliente Existente por Nombre:")
    nombre_buscar = input("Ingrese el Nombre o parte del Nombre del Cliente a Actualizar: ").lower()
    clientes_encontrados = []
    for cliente in clientes_matriz[1:]:
        if nombre_buscar == cliente[1].lower():
            clientes_encontrados.append(cliente)
    if len(clientes_encontrados) == 1:
        cliente = clientes_encontrados[0]
        print(f"Cliente Encontrado: {cliente[1]} {cliente[2]}")
        nuevo_nombre = input("Ingrese Nuevo Nombre (dejar en blanco para no cambiar): ")
        nuevo_apellido = input("Ingrese Nuevo Apellido (dejar en blanco para no cambiar): ")
        nuevo_email = input("Ingrese Nuevo Email (dejar en blanco para no cambiar): ")
        nuevo_telefono = input("Ingrese Nuevo Teléfono (dejar en blanco para no cambiar): ")

        if nuevo_nombre:
            cliente[1] = nuevo_nombre
        if nuevo_apellido:
            cliente[2] = nuevo_apellido
        if nuevo_email:
            cliente[3] = nuevo_email
        if nuevo_telefono:
            cliente[4] = nuevo_telefono

        print(f"¡Cliente '{cliente[1]} {cliente[2]}' actualizado con éxito!")
    elif len(clientes_encontrados) > 1:
        print("Se encontraron múltiples clientes con ese nombre. Por favor, utilice la opción de actualización por ID.")
    else:
        print(f"No se encontró ningún cliente con el nombre '{nombre_buscar}'. Por favor utilice la opción de buscar cliente por id o agregar cliente si desea crear uno nuevo.")

#--------------------------------------------------
#Funcion para eliminar cliente (cruD)
def eliminarCliente(clientes_matriz):
    print("Eliminar Cliente Existente:")
    id_buscar = int(input("Ingrese ID del Cliente a Eliminar: "))
    seEncontro = False
    for i, cliente in enumerate(clientes_matriz[1:], start=1):
        if cliente[0] == id_buscar:
            confirmacion = input(f"¿Está seguro que desea eliminar al cliente '{cliente[1]} {cliente[2]}'? (s/n): ").lower()
            if confirmacion == 's':
                clientes_matriz.pop(i)
                print(f"¡Cliente ID {id_buscar} eliminado con éxito!")
            else:
                print("Eliminación cancelada.")
            seEncontro = True
            break
    if not seEncontro:
        print(f"No se encontró ningún cliente con ID {id_buscar}.")
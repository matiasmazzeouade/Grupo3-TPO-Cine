import peliculasCrud, clientesCrud, funcionesCrud, reservasCrud, salasCrud, funciones, estadisticas

# Impresión de todas las listas de diccionarios
def imprimirListas():
    funciones.imprimir_lista_diccionarios("Listado de Películas", peliculas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Clientes", clientes_lista)
    funciones.imprimir_lista_diccionarios("Listado de Funciones", funciones_lista)
    funciones.imprimir_lista_diccionarios("Listado de Salas", salas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Reservas", reservas_lista)

def menu_crud(titulo, modulo, lista):
    sub_opcion = ''
    while sub_opcion != 'x':
        print(f"\n--- CRUD de {titulo} ---")
        print("a. Agregar")
        print("b. Consultar")
        print("c. Actualizar")
        print("d. Eliminar")
        sub_opcion = input(f"Seleccione una opción (a-d) o 'x' para volver al menú principal: ").lower()

        if sub_opcion == 'a':
            if titulo == 'Películas':
                modulo.agregarPelicula(lista)
            elif titulo == 'Clientes':
                modulo.agregarCliente(lista)
            elif titulo == 'Funciones':
                modulo.agregarFuncion(lista, peliculas_lista, salas_lista)
            elif titulo == 'Salas':
                 modulo.agregarSala(lista)
            elif titulo == 'Reservas':
                modulo.agregarReserva(lista, funciones_lista, clientes_lista)

        elif sub_opcion == 'b':
            # La mayoría de los módulos tienen consulta por ID, algunos tienen más opciones
            if titulo in ['Películas', 'Clientes', 'Funciones']:
                print("1. Consultar por ID")
                print("2. Consultar por Nombre/Fecha")
                op = input("Seleccione (1-2): ")
                if op == '1':
                    if titulo == 'Películas': modulo.leerPeliculaPorId(lista)
                    if titulo == 'Clientes': modulo.leerClientePorId(lista)
                    if titulo == 'Funciones': modulo.leerFuncionPorId(lista)
                elif op == '2':
                    if titulo == 'Películas': modulo.leerPeliculaPorNombre(lista)
                    if titulo == 'Clientes': modulo.leerClientePorNombre(lista)
                    if titulo == 'Funciones': modulo.leerFuncionesPorFecha(lista)
            else: # Salas y Reservas solo por ID
                if titulo == 'Salas': modulo.leerSalaPorId(lista)
                if titulo == 'Reservas': modulo.leerReservaPorId(lista)

        elif sub_opcion == 'c':
            if titulo == 'Películas':
                modulo.actualizarPelicula(lista)
            elif titulo == 'Clientes':
                 modulo.actualizarClientePorId(lista)
            elif titulo == 'Funciones':
                 modulo.actualizarFuncionPorId(lista, peliculas_lista, salas_lista)
            elif titulo == 'Salas':
                 modulo.actualizarSala(lista)
            elif titulo == 'Reservas':
                 modulo.actualizarReserva(lista, funciones_lista, clientes_lista)

        elif sub_opcion == 'd':
            if titulo == 'Películas':
                modulo.eliminarPelicula(lista)
            elif titulo == 'Clientes':
                modulo.eliminarCliente(lista)
            elif titulo == 'Funciones':
                 modulo.eliminarFuncion(lista)
            elif titulo == 'Salas':
                 modulo.eliminarSala(lista, funciones_lista)
            elif titulo == 'Reservas':
                modulo.eliminarReserva(lista)
        
        elif sub_opcion != 'x':
            print("Opción inválida. Intente nuevamente.")


def imprimirMenu():
    opcion = 0
    while opcion != -1:
        print("\n--- MENÚ PRINCIPAL DEL CINE ---")
        print("1. Ver Listados Completos")
        print("2. Gestión de Películas")
        print("3. Gestión de Clientes")
        print("4. Gestión de Funciones")
        print("5. Gestión de Salas")
        print("6. Gestión de Reservas")
        print("7. Ver Estadísticas")
        opcion = int(input("Seleccione una opción (1-7) o '-1' para salir: "))
        
        if opcion == 1:
            imprimirListas()
        elif opcion == 2:
            menu_crud("Películas", peliculasCrud, peliculas_lista)
        elif opcion == 3:
            menu_crud("Clientes", clientesCrud, clientes_lista)
        elif opcion == 4:
            menu_crud("Funciones", funcionesCrud, funciones_lista)
        elif opcion == 5:
            menu_crud("Salas", salasCrud, salas_lista)
        elif opcion == 6:
            menu_crud("Reservas", reservasCrud, reservas_lista)
        elif opcion == 7:
            estadisticas.mostrar_estadisticas(peliculas_lista, clientes_lista, funciones_lista, reservas_lista, salas_lista)
        elif opcion == -1:
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Intente de nuevo.")


# --- Definición de Cabeceras y Datos ---
peliculas_header = ['ID_Pelicula', 'Titulo', 'Genero', 'Duracion_min', 'Clasificacion']
peliculas_data = [
    [1, 'El Origen', 'Ciencia Ficción', 148, '+13'],
    [2, 'Parasitos', 'Suspenso', 132, '+16'],
    [3, 'Interestelar', 'Ciencia Ficción', 169, '+13'],
    [4, 'Mi Villano Favorito', 'Animación', 95, 'ATP'],
    [5, 'La La Land', 'Musical', 128, 'ATP']
]

clientes_header = ['ID_Cliente', 'Nombre', 'Apellido', 'Email', 'Telefono', 'Edad']
clientes_data = [
    [101, 'Ana', 'Gomez', 'ana.gomez@email.com', '1122334455', 30],
    [102, 'Carlos', 'Ruiz', 'carlos.r@email.com', '1122334456', 25],
    [103, 'Lucia', 'Fernandez', 'lucia.f@email.com', '1122334457', 45],
    [104, 'Marcos', 'Perez', 'marcos.p@email.com', '1122334458', 22],
    [105, 'Sofia', 'Martinez', 'sofia.m@email.com', '1122334459', 38]
]

funciones_header = ['ID_Funcion', 'ID_Pelicula', 'ID_Sala', 'Horario', 'Fecha']
funciones_data = [
    [501, 1, 2, '20:30', '2025-08-15'],
    [502, 3, 1, '21:00', '2025-08-15'],
    [503, 4, 3, '18:00', '2025-08-16'],
    [504, 2, 2, '22:15', '2025-08-16'],
    [505, 5, 4, '19:45', '2025-08-17']
]

reservas_header = ['ID_Reserva', 'ID_Funcion', 'ID_Cliente', 'Asientos', 'Fecha_Reserva']
reservas_data = [
    [1001, 501, 102, 'F5, F6', '2025-08-11'],
    [1002, 503, 101, 'C1, C2, C3', '2025-08-11'],
    [1003, 502, 104, 'H9', '2025-08-12'],
    [1004, 501, 103, 'G1', '2025-08-13'],
    [1005, 505, 105, 'D7, D8', '2025-08-14']
]

salas_header = ['ID_Sala', 'Nombre_Sala', 'Capacidad', 'Tipo']
salas_data = [
    [1, 'Sala 1', 100, '2D'],
    [2, 'Sala 2', 80, '3D'],
    [3, 'Sala 3', 50, 'IMAX'],
    [4, 'Sala 4', 120, '4DX']
]

# --- Conversión a Lista de Diccionarios usando zip ---
peliculas_lista = [dict(zip(peliculas_header, row)) for row in peliculas_data]
clientes_lista = [dict(zip(clientes_header, row)) for row in clientes_data]
funciones_lista = [dict(zip(funciones_header, row)) for row in funciones_data]
reservas_lista = [dict(zip(reservas_header, row)) for row in reservas_data]
salas_lista = [dict(zip(salas_header, row)) for row in salas_data]

# --- Iniciar el programa ---
imprimirMenu()

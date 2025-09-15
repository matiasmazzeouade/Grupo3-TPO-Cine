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
    [5, 'La La Land', 'Musical', 128, 'ATP'],
    [6, 'Avengers: Endgame', 'Acción', 181, '+13'],
    [7, 'Titanic', 'Drama', 195, '+13'],
    [8, 'Toy Story', 'Animación', 81, 'ATP'],
    [9, 'Matrix', 'Ciencia Ficción', 136, '+16'],
    [10, 'Joker', 'Drama', 122, '+16'],
    [11, 'Gladiador', 'Acción', 155, '+16'],
    [12, 'Coco', 'Animación', 105, 'ATP'],
    [13, 'Frozen', 'Animación', 102, 'ATP'],
    [14, 'El Padrino', 'Drama', 175, '+16'],
    [15, 'Duna', 'Ciencia Ficción', 155, '+13'],
    [16, 'Shrek', 'Animación', 90, 'ATP'],
    [17, 'Los Increíbles', 'Animación', 115, 'ATP'],
    [18, 'Harry Potter y la Piedra Filosofal', 'Fantasía', 152, 'ATP'],
    [19, 'Avatar', 'Ciencia Ficción', 162, '+13'],
    [20, 'Black Panther', 'Acción', 134, '+13']
]

clientes_header = ['ID_Cliente', 'Nombre', 'Apellido', 'Email', 'Telefono', 'Edad']
clientes_data = [
    [101, 'Ana', 'Gomez', 'ana.gomez@email.com', '1122334455', 30],
    [102, 'Carlos', 'Ruiz', 'carlos.r@email.com', '1122334456', 25],
    [103, 'Lucia', 'Fernandez', 'lucia.f@email.com', '1122334457', 45],
    [104, 'Marcos', 'Perez', 'marcos.p@email.com', '1122334458', 22],
    [105, 'Sofia', 'Martinez', 'sofia.m@email.com', '1122334459', 38],
    [106, 'Juan', 'Lopez', 'juan.lopez@email.com', '1122334460', 27],
    [107, 'Camila', 'Torres', 'camila.t@email.com', '1122334461', 33],
    [108, 'Diego', 'Romero', 'diego.r@email.com', '1122334462', 40],
    [109, 'Valentina', 'Alvarez', 'valen.a@email.com', '1122334463', 29],
    [110, 'Mateo', 'Suarez', 'mateo.s@email.com', '1122334464', 20],
    [111, 'Florencia', 'Cabrera', 'flor.c@email.com', '1122334465', 26],
    [112, 'Javier', 'Mendez', 'javier.m@email.com', '1122334466', 36],
    [113, 'Martina', 'Silva', 'martina.s@email.com', '1122334467', 31],
    [114, 'Tomas', 'Herrera', 'tomas.h@email.com', '1122334468', 23],
    [115, 'Paula', 'Diaz', 'paula.d@email.com', '1122334469', 42],
    [116, 'Agustin', 'Ramos', 'agustin.r@email.com', '1122334470', 19],
    [117, 'Julieta', 'Morales', 'julieta.m@email.com', '1122334471', 28],
    [118, 'Nicolas', 'Vega', 'nicolas.v@email.com', '1122334472', 37],
    [119, 'Laura', 'Ortega', 'laura.o@email.com', '1122334473', 41],
    [120, 'Pedro', 'Castro', 'pedro.c@email.com', '1122334474', 34]
]

funciones_header = ['ID_Funcion', 'ID_Pelicula', 'ID_Sala', 'Horario', 'Fecha']
funciones_data = [
    [501, 1, 2, '20:30', '2025-08-15'],
    [502, 3, 1, '21:00', '2025-08-15'],
    [503, 4, 3, '18:00', '2025-08-16'],
    [504, 2, 2, '22:15', '2025-08-16'],
    [505, 5, 4, '19:45', '2025-08-17'],
    [506, 6, 1, '20:00', '2025-08-18'],
    [507, 7, 3, '21:30', '2025-08-18'],
    [508, 8, 2, '17:00', '2025-08-19'],
    [509, 9, 4, '22:00', '2025-08-19'],
    [510, 10, 1, '19:00', '2025-08-20'],
    [511, 11, 2, '20:15', '2025-08-20'],
    [512, 12, 3, '18:30', '2025-08-21'],
    [513, 13, 4, '16:00', '2025-08-21'],
    [514, 14, 1, '21:45', '2025-08-22'],
    [515, 15, 2, '22:30', '2025-08-22'],
    [516, 16, 3, '17:30', '2025-08-23'],
    [517, 17, 4, '20:45', '2025-08-23'],
    [518, 18, 1, '19:15', '2025-08-24'],
    [519, 19, 2, '21:00', '2025-08-24'],
    [520, 20, 3, '22:45', '2025-08-25']
]

reservas_header = ['ID_Reserva', 'ID_Funcion', 'ID_Cliente', 'Asientos', 'Fecha_Reserva']
reservas_data = [
    [1001, 501, 102, 'F5, F6', '2025-08-11'],
    [1002, 503, 101, 'C1, C2, C3', '2025-08-11'],
    [1003, 502, 104, 'H9', '2025-08-12'],
    [1004, 501, 103, 'G1', '2025-08-13'],
    [1005, 505, 105, 'D7, D8', '2025-08-14'],
    [1006, 506, 106, 'A1, A2', '2025-08-14'],
    [1007, 507, 107, 'B3, B4', '2025-08-15'],
    [1008, 508, 108, 'C5', '2025-08-15'],
    [1009, 509, 109, 'D1, D2', '2025-08-16'],
    [1010, 510, 110, 'E6, E7, E8', '2025-08-16'],
    [1011, 511, 111, 'F9', '2025-08-17'],
    [1012, 512, 112, 'G2, G3', '2025-08-17'],
    [1013, 513, 113, 'H1, H2, H3', '2025-08-18'],
    [1014, 514, 114, 'J5', '2025-08-18'],
    [1015, 515, 115, 'K6, K7', '2025-08-19'],
    [1016, 516, 116, 'L1, L2', '2025-08-19'],
    [1017, 517, 117, 'M3', '2025-08-20'],
    [1018, 518, 118, 'N4, N5, N6', '2025-08-20'],
    [1019, 519, 119, 'O1, O2', '2025-08-21'],
    [1020, 520, 120, 'P7, P8', '2025-08-21']
]

salas_header = ['ID_Sala', 'Nombre_Sala', 'Capacidad', 'Tipo']
salas_data = [
    [1, 'Sala 1', 100, '2D'],
    [2, 'Sala 2', 80, '3D'],
    [3, 'Sala 3', 50, 'IMAX'],
    [4, 'Sala 4', 120, '4DX'],
    [5, 'Sala 5', 150, '2D'],
    [6, 'Sala 6', 90, '3D'],
    [7, 'Sala 7', 60, '2D'],
    [8, 'Sala 8', 200, 'IMAX'],
    [9, 'Sala 9', 75, '4DX'],
    [10, 'Sala 10', 110, '2D'],
    [11, 'Sala 11', 95, '3D'],
    [12, 'Sala 12', 130, 'IMAX'],
    [13, 'Sala 13', 55, '2D'],
    [14, 'Sala 14', 170, '4DX'],
    [15, 'Sala 15', 140, '2D'],
    [16, 'Sala 16', 100, '3D'],
    [17, 'Sala 17', 80, 'IMAX'],
    [18, 'Sala 18', 65, '2D'],
    [19, 'Sala 19', 190, '4DX'],
    [20, 'Sala 20', 125, '2D']
]

# --- Conversión a Lista de Diccionarios usando zip ---
peliculas_lista = [dict(zip(peliculas_header, row)) for row in peliculas_data]
clientes_lista = [dict(zip(clientes_header, row)) for row in clientes_data]
funciones_lista = [dict(zip(funciones_header, row)) for row in funciones_data]
reservas_lista = [dict(zip(reservas_header, row)) for row in reservas_data]
salas_lista = [dict(zip(salas_header, row)) for row in salas_data]

# --- Iniciar el programa ---
imprimirMenu()

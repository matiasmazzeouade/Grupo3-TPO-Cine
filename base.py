import peliculasCrud, funciones




# Impresión de matrices
def imprimirMatrices():
    funciones.imprimir_matriz("Matriz de Películas", peliculas_matriz)
    funciones.imprimir_matriz("Matriz de Clientes", clientes_matriz)
    funciones.imprimir_matriz("Matriz de Funciones", funciones_matriz)
    funciones.imprimir_matriz("Matriz de Reservas", reservas_matriz)

def imprimirMenu():
    opcion = 0
    while opcion != -1:    
        print("Menú de Opciones:")
        print("1. Ver Matrices")
        print("2. Crud de Películas")
        print("3. Crud de Clientes")
        print("4. Crud de Funciones")
        print("5. Crud de Reservas")
        opcion = int(input("Seleccione una opción (1-5) o '-1' para salir: "))
        match opcion:
            case 1:
                imprimirMatrices()
            case 2:
                sub_opcion = ''
                while sub_opcion not in ['a', 'b', 'c', 'd', 'x']:
                    print("CRUD de Películas:")
                    print("a. Agregar Película")
                    print("b. Consultar Película")
                    print("c. Actualizar Película")
                    print("d. Eliminar Película")
                    sub_opcion = input("Seleccione una opción (a-d) o 'x' para volver al menú principal: ").lower()
                    match sub_opcion:
                        case 'a':
                            peliculasCrud.agregarPelicula(peliculas_matriz)
                        case 'b':
                            print("Opciones de Consulta:")
                            print("1. Buscar por ID")
                            print("2. Buscar por Nombre")
                            metodo_consulta = input("Seleccione una opción (1-2): ")
                            match metodo_consulta:
                                case '1':
                                    peliculasCrud.leerPeliculaPorId(peliculas_matriz)
                                case '2':
                                    peliculasCrud.leerPeliculaPorNombre(peliculas_matriz)
                                case _:
                                    print("Opción inválida. Volviendo al menú CRUD de Películas.")
                        case 'c':
                            peliculasCrud.actualizarPelicula(peliculas_matriz)
                        case 'd':
                            peliculasCrud.eliminarPelicula(peliculas_matriz)
                        case 'x':
                            return
                        case _:
                            print("Opción inválida. Intente nuevamente.")
                        
            case 3:
                print("CRUD de Clientes: (Funcionalidad no implementada aún)")
            case 4:
                print("CRUD de Funciones: (Funcionalidad no implementada aún)")
            case 5:
                print("CRUD de Reservas: (Funcionalidad no implementada aún)")
            case -1:
                print("Saliendo del programa. ¡Hasta luego!")




# 1. Matriz de Películas
peliculas_matriz = [
    ['ID_Pelicula', 'Titulo', 'Genero', 'Duracion_min', 'Clasificacion'],
    [1, 'El Origen', 'Ciencia Ficción', 148, '+13'],
    [2, 'Parasitos', 'Suspenso', 132, '+16'],
    [3, 'Interestelar', 'Ciencia Ficción', 169, '+13'],
    [4, 'Mi Villano Favorito', 'Animación', 95, 'ATP'],
    [5, 'La La Land', 'Musical', 128, 'ATP']
]

# 2. Matriz de Clientes
clientes_matriz = [
    ['ID_Cliente', 'Nombre', 'Apellido', 'Email'],
    [101, 'Ana', 'Gomez', 'ana.gomez@email.com'],
    [102, 'Carlos', 'Ruiz', 'carlos.r@email.com'],
    [103, 'Lucia', 'Fernandez', 'lucia.f@email.com'],
    [104, 'Marcos', 'Perez', 'marcos.p@email.com'],
    [105, 'Sofia', 'Martinez', 'sofia.m@email.com']
]

# 3. Matriz de Funciones
funciones_matriz = [
    ['ID_Funcion', 'ID_Pelicula', 'ID_Sala', 'Horario', 'Fecha'],
    [501, 1, 2, '20:30', '2025-08-15'],
    [502, 3, 1, '21:00', '2025-08-15'],
    [503, 4, 3, '18:00', '2025-08-16'],
    [504, 2, 2, '22:15', '2025-08-16'],
    [505, 5, 4, '19:45', '2025-08-17']
]

# 4. Matriz de Reservas
reservas_matriz = [
    ['ID_Reserva', 'ID_Funcion', 'ID_Cliente', 'Asientos', 'Fecha_Reserva'],
    [1001, 501, 102, 'F5, F6', '2025-08-11'],
    [1002, 503, 101, 'C1, C2, C3', '2025-08-11'],
    [1003, 502, 104, 'H9', '2025-08-12'],
    [1004, 501, 103, 'G1', '2025-08-13'],
    [1005, 505, 105, 'D7, D8', '2025-08-14']
]

# 5. Matriz de Salas
salas_matriz = [
    ['ID_Sala', 'Nombre_Sala', 'Capacidad', 'Tipo'],
    [1, 'Sala 1', 100, '2D'],
    [2, 'Sala 2', 80, '3D'],
    [3, 'Sala 3', 50, 'IMAX'],
    [4, 'Sala 4', 120, '4DX']
]

imprimirMenu()
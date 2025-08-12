def imprimir_matriz(titulo, matriz):
    print(f"\n{titulo}:")
    #FALTA
     
     
     
     
     
     
        
# --- 1. Matriz de Películas ---
# Columnas: ID_Pelicula (int), Titulo (str), Genero (str), Duracion_min (int), Clasificacion (str)
peliculas_matriz = [
    ['ID_Pelicula', 'Titulo', 'Genero', 'Duracion_min', 'Clasificacion'],
    [1, 'El Origen', 'Ciencia Ficción', 148, '+13'],
    [2, 'Parasitos', 'Suspenso', 132, '+16'],
    [3, 'Interestelar', 'Ciencia Ficción', 169, '+13'],
    [4, 'Mi Villano Favorito', 'Animación', 95, 'ATP'],
    [5, 'La La Land', 'Musical', 128, 'ATP']
]

# --- 2. Matriz de Clientes ---
# Columnas: ID_Cliente (int), Nombre (str), Apellido (str), Email (str)
clientes_matriz = [
    ['ID_Cliente', 'Nombre', 'Apellido', 'Email'],
    [101, 'Ana', 'Gomez', 'ana.gomez@email.com'],
    [102, 'Carlos', 'Ruiz', 'carlos.r@email.com'],
    [103, 'Lucia', 'Fernandez', 'lucia.f@email.com'],
    [104, 'Marcos', 'Perez', 'marcos.p@email.com'],
    [105, 'Sofia', 'Martinez', 'sofia.m@email.com']
]

# --- 3. Matriz de Funciones ---
# Columnas: ID_Funcion (int), ID_Pelicula (int), ID_Sala (int), Horario (str), Fecha (str)
funciones_matriz = [
    ['ID_Funcion', 'ID_Pelicula', 'ID_Sala', 'Horario', 'Fecha'],
    [501, 1, 2, '20:30', '2025-08-15'],
    [502, 3, 1, '21:00', '2025-08-15'],
    [503, 4, 3, '18:00', '2025-08-16'],
    [504, 2, 2, '22:15', '2025-08-16'],
    [505, 5, 4, '19:45', '2025-08-17']
]

# --- 4. Matriz de Reservas ---
# Columnas: ID_Reserva (int), ID_Funcion (int), ID_Cliente (int), Asientos (str), Fecha_Reserva (str)
reservas_matriz = [
    ['ID_Reserva', 'ID_Funcion', 'ID_Cliente', 'Asientos', 'Fecha_Reserva'],
    [1001, 501, 102, 'F5, F6', '2025-08-11'],
    [1002, 503, 101, 'C1, C2, C3', '2025-08-11'],
    [1003, 502, 104, 'H9', '2025-08-12'],
    [1004, 501, 103, 'G1', '2025-08-13'],
    [1005, 505, 105, 'D7, D8', '2025-08-14']
]


# --- Impresión de todas las matrices ---
imprimir_matriz("Matriz de Películas", peliculas_matriz)
imprimir_matriz("Matriz de Clientes", clientes_matriz)
imprimir_matriz("Matriz de Funciones", funciones_matriz)
imprimir_matriz("Matriz de Reservas", reservas_matriz)
import peliculasCrud, clientesCrud, funcionesCrud, reservasCrud, salasCrud, funciones, estadisticas
import json 

# Definición de nombres de archivos
PELICULAS_FILE = 'peliculas.json'
CLIENTES_FILE = 'clientes.json'
FUNCIONES_FILE = 'funciones.json'
SALAS_FILE = 'salas.json'
RESERVAS_FILE = 'reservas.json'

# Función para cargar datos desde JSON
def cargar_datos(archivo):
    """
    Carga datos desde un archivo JSON.
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    """
    try:
        with open(archivo, 'r', encoding="UTF-8") as f:
            datos = json.load(f) 
            return datos
    except FileNotFoundError: 
        print(f"Advertencia: El archivo '{archivo}' no se encontró. Se creará uno nuevo al guardar.")
        return [] 
    except json.JSONDecodeError: 
        print(f"Advertencia: El archivo '{archivo}' está vacío o corrupto. Se usará una lista vacía.")
        return []
    except Exception as e: 
        print(f"Error inesperado al cargar '{archivo}': {e}")
        return []

# Función para guardar datos en JSON
def guardar_datos(archivo, datos):
    """
    Guarda una lista de diccionarios en un archivo JSON.
    """
    try:
        with open(archivo, 'w', encoding="UTF-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4) 
    except (IOError, OSError) as e: 
        print(f"Error: No se pudo guardar el archivo '{archivo}'. Cambios no guardados.")
        print(f"Detalle: {e}")

# Impresión de todas las listas de diccionarios
def imprimirListas():
    funciones.imprimir_lista_diccionarios("Listado de Películas", peliculas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Clientes", clientes_lista)
    funciones.imprimir_lista_diccionarios("Listado de Funciones", funciones_lista)
    funciones.imprimir_lista_diccionarios("Listado de Salas", salas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Reservas", reservas_lista)

def menu_crud(titulo, modulo, lista, archivo_json):
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
            
            # Guardamos los cambios después de agregar
            guardar_datos(archivo_json, lista)

        elif sub_opcion == 'b':
            # (El consultar no modifica datos, no necesita guardar)
            if titulo in ['Películas', 'Clientes', 'Funciones']:
                print("1. Consultar por ID")
                print("2. Consultar por Nombre/Fecha")
                
                if titulo == 'Películas':
                    print("3. Ver primeras N películas")
                
                op = input("Seleccione: ")
                
                if op == '1':
                    if titulo == 'Películas': modulo.leerPeliculaPorId(lista)
                    if titulo == 'Clientes': modulo.leerClientePorId(lista)
                    if titulo == 'Funciones': modulo.leerFuncionPorId(lista)
                elif op == '2':
                    if titulo == 'Películas': modulo.leerPeliculaPorNombre(lista)
                    if titulo == 'Clientes': modulo.leerClientePorNombre(lista)
                    if titulo == 'Funciones': modulo.leerFuncionesPorFecha(lista)
                
                elif op == '3' and titulo == 'Películas':
                    try:
                        cantidad = int(input("¿Cuántas películas desea ver?: "))
                        modulo.leerPrimerasNPeliculas(lista, cantidad)
                    except ValueError as e:
                        print(f"Error: {e}") 
                
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

            # Guardamos los cambios después de actualizar
            guardar_datos(archivo_json, lista)

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
            
            # Guardamos los cambios después de eliminar
            guardar_datos(archivo_json, lista)
        
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
        try:
            opcion = int(input("Seleccione una opción (1-7) o '-1' para salir: "))
        except ValueError: 
            print("Error: debe ingresar un número.")
            continue
        
        if opcion == 1:
            imprimirListas()
        elif opcion == 2:
            menu_crud("Películas", peliculasCrud, peliculas_lista, PELICULAS_FILE)
        elif opcion == 3:
            menu_crud("Clientes", clientesCrud, clientes_lista, CLIENTES_FILE)
        elif opcion == 4:
            menu_crud("Funciones", funcionesCrud, funciones_lista, FUNCIONES_FILE)
        elif opcion == 5:
            menu_crud("Salas", salasCrud, salas_lista, SALAS_FILE)
        elif opcion == 6:
            menu_crud("Reservas", reservasCrud, reservas_lista, RESERVAS_FILE)
        elif opcion == 7:
            estadisticas.mostrar_estadisticas(peliculas_lista, clientes_lista, funciones_lista, reservas_lista, salas_lista)
        elif opcion == -1:
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Intente de nuevo.")


# Conversión a Lista de Diccionarios usando carga de archivos
peliculas_lista = cargar_datos(PELICULAS_FILE)
clientes_lista = cargar_datos(CLIENTES_FILE)
funciones_lista = cargar_datos(FUNCIONES_FILE)
reservas_lista = cargar_datos(RESERVAS_FILE)
salas_lista = cargar_datos(SALAS_FILE)

# Iniciar el programa 
imprimirMenu()
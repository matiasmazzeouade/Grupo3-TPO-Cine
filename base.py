import peliculasCrud, clientesCrud, funcionesCrud, reservasCrud, salasCrud, funciones, estadisticas
import premiosCrud     # ✅ NUEVO MÓDULO
import json

# -----------------------------
# ARCHIVOS
# -----------------------------
PELICULAS_FILE = 'peliculas.json'
CLIENTES_FILE = 'clientes.json'
FUNCIONES_FILE = 'funciones.json'
SALAS_FILE = 'salas.json'
RESERVAS_FILE = 'reservas.txt'   # ✅ TXT

# -----------------------------
# CARGA Y GUARDADO JSON
# -----------------------------
def cargar_datos(archivo):
    try:
        with open(archivo, 'r', encoding="UTF-8") as f:
            return json.load(f)
    except:
        return []

def guardar_datos(archivo, datos):
    try:
        with open(archivo, 'w', encoding="UTF-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error guardando '{archivo}': {e}")

# -----------------------------
# CARGA Y GUARDADO TXT (RESERVAS)
# -----------------------------
def cargar_reservas_txt():
    reservas = []

    try:
        with open(RESERVAS_FILE, "r", encoding="UTF-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if linea == "":
                    continue

                datos = linea.split(";")

                reserva = {
                    "ID_Reserva": int(datos[0]),
                    "ID_Funcion": int(datos[1]),
                    "ID_Cliente": int(datos[2]),
                    "Asientos": datos[3],
                    "Fecha_Reserva": datos[4]
                }

                reservas.append(reserva)

    except FileNotFoundError:
        reservas = []

    return reservas


def guardar_reservas_txt(reservas):
    with open(RESERVAS_FILE, "w", encoding="UTF-8") as archivo:
        for r in reservas:
            linea = (
                f"{r['ID_Reserva']};"
                f"{r['ID_Funcion']};"
                f"{r['ID_Cliente']};"
                f"{r['Asientos']};"
                f"{r['Fecha_Reserva']}\n"
            )
            archivo.write(linea)

# -----------------------------
# IMPRIMIR TODAS LAS LISTAS
# -----------------------------
def imprimirListas():
    funciones.imprimir_lista_diccionarios("Listado de Películas", peliculas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Clientes", clientes_lista)
    funciones.imprimir_lista_diccionarios("Listado de Funciones", funciones_lista)
    funciones.imprimir_lista_diccionarios("Listado de Salas", salas_lista)
    funciones.imprimir_lista_diccionarios("Listado de Reservas", reservas_lista)

    # ✅ Premios con lista de listas
    print("\n--- LISTADO DE PREMIOS (Lista de Listas) ---")
    if premios_lista:
        for p in premios_lista:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Año: {p[2]}")
    else:
        print("No hay premios cargados.")

# -----------------------------
# MENÚ PRINCIPAL
# -----------------------------
def imprimirMenu():
    op = 0
    while op != -1:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ver listados completos")
        print("2. Películas")
        print("3. Clientes")
        print("4. Funciones")
        print("5. Salas")
        print("6. Reservas")
        print("7. Estadísticas")
        print("8. Premios (lista de listas)")
        print("-1. Salir")

        try:
            op = int(input("Seleccione: "))
        except:
            print("Debe ingresar un número.")
            continue

        if op == 1:
            imprimirListas()

        # -------------------------
        # PELÍCULAS
        # -------------------------
        elif op == 2:
            peliculasCrud.menu_peliculas(
                peliculas_lista,
                funciones_lista,
                reservas_lista
            )
            guardar_datos(PELICULAS_FILE, peliculas_lista)
            guardar_datos(FUNCIONES_FILE, funciones_lista)
            guardar_reservas_txt(reservas_lista)

        # -------------------------
        # CLIENTES
        # -------------------------
        elif op == 3:
            clientesCrud.menu_clientes(
                clientes_lista,
                reservas_lista
            )
            guardar_datos(CLIENTES_FILE, clientes_lista)
            guardar_reservas_txt(reservas_lista)

        # -------------------------
        # FUNCIONES
        # -------------------------
        elif op == 4:
            funcionesCrud.menu_funciones(
                funciones_lista,
                peliculas_lista,
                salas_lista,
                reservas_lista
            )
            guardar_datos(FUNCIONES_FILE, funciones_lista)
            guardar_reservas_txt(reservas_lista)

        # -------------------------
        # SALAS
        # -------------------------
        elif op == 5:
            salasCrud.menu_salas(
                salas_lista,
                funciones_lista,
                reservas_lista
            )
            guardar_datos(SALAS_FILE, salas_lista)
            guardar_datos(FUNCIONES_FILE, funciones_lista)
            guardar_reservas_txt(reservas_lista)

        # -------------------------
        # RESERVAS
        # -------------------------
        elif op == 6:
            reservasCrud.menu_reservas(
                reservas_lista,
                funciones_lista,
                clientes_lista
            )
            guardar_reservas_txt(reservas_lista)

        # -------------------------
        # ESTADÍSTICAS
        # -------------------------
        elif op == 7:
            estadisticas.mostrar_estadisticas(
                peliculas_lista,
                clientes_lista,
                funciones_lista,
                reservas_lista,
                salas_lista
            )

        # -------------------------
        # PREMIOS
        # -------------------------
        elif op == 8:
            premiosCrud.menu_premios(premios_lista)

        elif op == -1:
            print("Saliendo...")

# -----------------------------
# CARGA DE ARCHIVOS
# -----------------------------
peliculas_lista = cargar_datos(PELICULAS_FILE)
clientes_lista = cargar_datos(CLIENTES_FILE)
funciones_lista = cargar_datos(FUNCIONES_FILE)
salas_lista = cargar_datos(SALAS_FILE)
reservas_lista = cargar_reservas_txt()   # ✅ TXT

# -----------------------------
# LISTA DE PREMIOS
# -----------------------------
premios_lista = [
    [1, "Premio a la Mejor Sala 3D", 2023],
    [2, "Cliente del Año", 2024],
    [3, "Premio al Mejor Estreno", 2025]
]

# -----------------------------
# INICIO DEL PROGRAMA
# -----------------------------
imprimirMenu()

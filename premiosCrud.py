# --------------------------------------------------
# CRUD DE PREMIOS (LISTA DE LISTAS + RECURSIVIDAD)
# --------------------------------------------------

# Estructura de premios_lista:
# [ [ID, Nombre_Premio, Año], [...], ... ]

def agregarPremio(premios_lista):
    print("Agregar Nuevo Premio:")

    nuevo_id = premios_lista[-1][0] + 1 if premios_lista else 1

    nombre = input("Ingrese nombre del premio: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        año = int(input("Ingrese año del premio: "))
    except:
        print("El año debe ser numérico.")
        return

    premios_lista.append([nuevo_id, nombre, año])
    print(f"Premio '{nombre}' agregado correctamente.")


# ------------------------------
# RECURSIVIDAD FORZADA
# ------------------------------

def _buscar_premio_recursivo(lista, nombre_buscar):
    """
    Búsqueda recursiva en LISTA DE LISTAS.
    Fuerza recursión para cumplir la consigna.
    """
    if not lista:
        return None

    actual = lista[0]

    if nombre_buscar.lower() in actual[1].lower():
        return actual

    return _buscar_premio_recursivo(lista[1:], nombre_buscar)


def leerPremioPorNombre(premios_lista):
    nombre = input("Ingrese nombre del premio a buscar: ").strip()
    resultado = _buscar_premio_recursivo(premios_lista, nombre)

    if resultado:
        print(f"Premio encontrado → ID: {resultado[0]}, Nombre: {resultado[1]}, Año: {resultado[2]}")
    else:
        print("No se encontró el premio.")


def listarPremios(premios_lista):
    print("\n--- LISTADO DE PREMIOS ---")
    if not premios_lista:
        print("No hay premios cargados.")
        return

    for p in premios_lista:
        print(f"ID: {p[0]} | Nombre: {p[1]} | Año: {p[2]}")


def menu_premios(premios_lista):
    op = ""
    while op != "x":
        print("\n--- Gestión de Premios (Lista de Listas) ---")
        print("1. Agregar premio")
        print("2. Buscar por nombre (recursivo)")
        print("3. Ver listado")
        print("x. Volver")

        op = input("Seleccione: ").lower()

        if op == "1":
            agregarPremio(premios_lista)
        elif op == "2":
            leerPremioPorNombre(premios_lista)
        elif op == "3":
            listarPremios(premios_lista)
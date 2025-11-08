#Grupillo Marcos

import pytest  # Importamos pytest
import clientesCrud  # Importamos el módulo a probar

# --- DATOS DE PRUEBA ---
lista_prueba = [
    {"ID_Cliente": 101, "Nombre": "Ana", "Apellido": "Gomez", "Email": "ana@email.com", "Telefono": "111", "Edad": 30},
    {"ID_Cliente": 102, "Nombre": "Carlos", "Apellido": "Ruiz", "Email": "carlos@email.com", "Telefono": "222", "Edad": 25},
    {"ID_Cliente": 103, "Nombre": "Lucia", "Apellido": "Fernandez", "Email": "lucia@email.com", "Telefono": "333", "Edad": 45}
]

# --- PRUEBA ---

def test_buscar_cliente_recursiva_encontrado():
    """
    Prueba que la función recursiva encuentre un cliente que SÍ existe.
    """
    print("Ejecutando: test_buscar_cliente_recursiva_encontrado")

    # 1. PREPARACIÓN
    id_a_buscar = 102

    # 2. EJECUCIÓN
    cliente = clientesCrud._buscar_cliente_recursiva(lista_prueba, id_a_buscar)

    # 3. VERIFICACIÓN
    assert cliente is not None
    assert cliente["ID_Cliente"] == 102
    assert cliente["Nombre"] == "Carlos"


def test_buscar_cliente_recursiva_no_encontrado():
    """
    Prueba que la función recursiva devuelva 'None' si el cliente NO existe.
    """
    print("Ejecutando: test_buscar_cliente_recursiva_no_encontrado")

    # 1. PREPARACIÓN
    id_a_buscar = 999

    # 2. EJECUCIÓN
    cliente = clientesCrud._buscar_cliente_recursiva(lista_prueba, id_a_buscar)

    # 3. VERIFICACIÓN
    assert cliente is None


def test_ultimos_dos_clientes_error():
    """
    Prueba que la función lance un ValueError si hay menos de 2 clientes.
    """
    print("Ejecutando: test_ultimos_dos_clientes_error")

    # 1. PREPARACIÓN
    lista_corta = [{"ID_Cliente": 101, "Nombre": "Ana"}]  # Solo 1 cliente

    # 2. EJECUCIÓN Y VERIFICACIÓN
    with pytest.raises(ValueError):
        clientesCrud.leerUltimosDosClientes(lista_corta)

#Mazzeo Matías

# test_reservas.py
import pytest
from datetime import date
from reservasCrud import (
    agregarReserva,
    leerReservaPorId,
    eliminarReserva
)

# ------------------------------------------------------------
# TEST 1 — leerReservaPorId (reserva existente)
# ------------------------------------------------------------
def test_leer_reserva_por_id_encontrada(monkeypatch, capsys):
    reservas = [
        {
            'ID_Reserva': 1001,
            'ID_Funcion': 10,
            'ID_Cliente': 1,
            'Asientos': 'F5',
            'Fecha_Reserva': '2024-11-10'
        }
    ]

    # Simula input del usuario
    monkeypatch.setattr('builtins.input', lambda _: "1001")

    leerReservaPorId(reservas)
    captured = capsys.readouterr().out

    assert "Consultar Reserva por ID" in captured
    assert "Reserva Encontrada" in captured
    assert "1001" in captured
    assert "10" in captured
    assert "1" in captured
    assert "F5" in captured


# ------------------------------------------------------------
# TEST 2 — eliminarReserva (confirmación = 's')
# ------------------------------------------------------------
def test_eliminar_reserva_confirmada(monkeypatch, capsys):
    reservas = [
        {'ID_Reserva': 1001, 'ID_Funcion': 10, 'ID_Cliente': 1, 'Asientos': 'F5', 'Fecha_Reserva': '2024-11-10'},
        {'ID_Reserva': 1002, 'ID_Funcion': 11, 'ID_Cliente': 2, 'Asientos': 'F6', 'Fecha_Reserva': '2024-11-11'}
    ]

    # Secuencia de inputs: ID que se elimina -> confirmación
    inputs = iter(["1001", "s"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    eliminarReserva(reservas)
    captured = capsys.readouterr().out

    # Validaciones
    assert len(reservas) == 1
    assert reservas[0]['ID_Reserva'] == 1002
    assert "eliminada" in captured.lower()


# ------------------------------------------------------------
# TEST 3 — agregarReserva (caso correcto)
# ------------------------------------------------------------
def test_agregar_reserva_correcta(monkeypatch, capsys):
    reservas = []
    funciones = [{'ID_Funcion': 10}]
    clientes = [{'ID_Cliente': 1}]

    # Secuencia: ID Función -> ID Cliente -> Asiento
    inputs = iter(["10", "1", "F5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    agregarReserva(reservas, funciones, clientes)
    captured = capsys.readouterr().out

    # La reserva se agregó
    assert "agregada correctamente" in captured
    assert len(reservas) == 1

    nueva = reservas[0]

    # Verificaciones de los datos agregados
    assert nueva['ID_Reserva'] == 1001
    assert nueva['ID_Funcion'] == 10
    assert nueva['ID_Cliente'] == 1
    assert nueva['Asientos'] == "F5"

    # Fecha actual
    assert nueva['Fecha_Reserva'] == date.today().isoformat()

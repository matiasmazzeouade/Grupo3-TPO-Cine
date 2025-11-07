import pytest
import salasCrud  # Importa tu módulo con las funciones CRUD

# --- DATOS DE PRUEBA ---
salas_lista = [
    {'ID_Sala': 1, 'Nombre_Sala': 'Sala 1', 'Capacidad': 100, 'Tipo': '2D'},
    {'ID_Sala': 2, 'Nombre_Sala': 'Sala 2', 'Capacidad': 200, 'Tipo': '3D'}
]

funciones_lista = [
    {'ID_Funcion': 1, 'ID_Sala': 2}
]


# --------------------------------------------------
# Test: agregarSala
# --------------------------------------------------
def test_agregar_sala(monkeypatch, capsys):
    """
    Prueba que agregarSala agregue una nueva sala correctamente.
    """
    entradas = iter(["Sala 3", "150", "IMAX"])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    salas = salas_lista.copy()
    salasCrud.agregarSala(salas)

    out = capsys.readouterr().out
    assert "Sala 'Sala 3' agregada." in out
    assert len(salas) == 3
    assert salas[-1]['Nombre_Sala'] == "Sala 3"
    assert salas[-1]['Capacidad'] == 150
    assert salas[-1]['Tipo'] == "IMAX"


# --------------------------------------------------
# Test: leerSalaPorId
# --------------------------------------------------
def test_leer_sala_existente(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    salasCrud.leerSalaPorId(salas_lista)
    out = capsys.readouterr().out
    assert "Sala Encontrada" in out


def test_leer_sala_inexistente(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    salasCrud.leerSalaPorId(salas_lista)
    out = capsys.readouterr().out
    assert "No se encontró" in out


# --------------------------------------------------
# Test: actualizarSala
# --------------------------------------------------
def test_actualizar_sala(monkeypatch, capsys):
    """
    Prueba que actualizarSala modifique los datos correctamente.
    """
    entradas = iter(["1", "Sala Renovada", "120", "4D"])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    salas = salas_lista.copy()
    salasCrud.actualizarSala(salas)
    out = capsys.readouterr().out

    assert "actualizada" in out
    assert salas[0]['Nombre_Sala'] == "Sala Renovada"
    assert salas[0]['Capacidad'] == 120
    assert salas[0]['Tipo'] == "4D"


def test_actualizar_sala_inexistente(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "99")
    salasCrud.actualizarSala(salas_lista)
    out = capsys.readouterr().out
    assert "No se encontró" in out


# --------------------------------------------------
# Test: eliminarSala
# --------------------------------------------------
def test_eliminar_sala_confirmada(monkeypatch, capsys):
    """
    Prueba que se elimine una sala correctamente cuando el usuario confirma.
    """
    entradas = iter(["1", "s"])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    salas = salas_lista.copy()
    funciones = []
    salasCrud.eliminarSala(salas, funciones)
    out = capsys.readouterr().out

    assert "eliminada" in out
    assert len(salas) == 1


def test_eliminar_sala_cancelada(monkeypatch, capsys):
    entradas = iter(["1", "n"])
    monkeypatch.setattr('builtins.input', lambda _: next(entradas))
    
    salas = salas_lista.copy()
    funciones = []
    salasCrud.eliminarSala(salas, funciones)
    out = capsys.readouterr().out

    assert "cancelada" in out
    assert len(salas) == 2


def test_eliminar_sala_en_uso(monkeypatch, capsys):
    """
    Prueba que no se pueda eliminar una sala que tiene funciones asignadas.
    """
    monkeypatch.setattr('builtins.input', lambda _: "2")
    salasCrud.eliminarSala(salas_lista.copy(), funciones_lista)
    out = capsys.readouterr().out
    assert "no se puede eliminar" in out.lower()


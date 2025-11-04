import pytest # Importamos pytest
import peliculasCrud # Importamos el módulo que queremos probar

# --- DATOS DE PRUEBA ---
# Creamos una lista de películas de prueba para usarla en nuestros tests
# Es una 'simulación' de nuestra base de datos
lista_prueba = [
    {'ID_Pelicula': 1, 'Titulo': 'El Origen', 'Genero': 'Ciencia Ficción', 'Duracion_min': 148, 'Clasificacion': '+13'},
    {'ID_Pelicula': 2, 'Titulo': 'Parasitos', 'Genero': 'Suspenso', 'Duracion_min': 132, 'Clasificacion': '+16'},
    {'ID_Pelicula': 3, 'Titulo': 'Interestelar', 'Genero': 'Ciencia Ficción', 'Duracion_min': 169, 'Clasificacion': '+13'}
]

# --- PRUEBAS UNITARIAS (Clase 10) ---

def test_buscar_pelicula_recursiva_encontrada():
    """
    Prueba que la función recursiva encuentre una película que SÍ existe.
    """
    print("Ejecutando: test_buscar_pelicula_recursiva_encontrada")
    # 1. PREPARACIÓN (Definir qué buscamos)
    id_a_buscar = 3
    
    # 2. EJECUCIÓN (Llamar a la función)
    pelicula = peliculasCrud._buscar_pelicula_recursiva(lista_prueba, id_a_buscar)
    
    # 3. VERIFICACIÓN (Comprobar con 'assert')
    # Comprobamos que la función NO devolvió None
    assert pelicula is not None 
    # Comprobamos que la película que encontró es la correcta
    assert pelicula['ID_Pelicula'] == 3
    assert pelicula['Titulo'] == 'Interestelar'

def test_buscar_pelicula_recursiva_no_encontrada():
    """
    Prueba que la función recursiva devuelva 'None' si la película NO existe.
    """
    print("Ejecutando: test_buscar_pelicula_recursiva_no_encontrada")
    # 1. PREPARACIÓN
    id_a_buscar = 99
    
    # 2. EJECUCIÓN
    pelicula = peliculasCrud._buscar_pelicula_recursiva(lista_prueba, id_a_buscar)
    
    # 3. VERIFICACIÓN
    # Comprobamos que la función devolvió None
    assert pelicula is None

def test_obtener_info_basica_pelicula():
    """
    Prueba que la función que devuelve una TUPLA funcione correctamente.
    """
    print("Ejecutando: test_obtener_info_basica_pelicula")
    # 1. PREPARACIÓN
    id_a_buscar = 2
    
    # 2. EJECUCIÓN
    info_tupla = peliculasCrud.obtener_info_basica_pelicula(lista_prueba, id_a_buscar)
    
    # 3. VERIFICACIÓN
    assert info_tupla is not None
    # Verificamos que sea una tupla
    assert isinstance(info_tupla, tuple)
    # Verificamos el contenido de la tupla
    assert info_tupla == ('Parasitos', 'Suspenso', '+16')

def test_slicing_leer_primeras_n_peliculas_error():
    """
    Prueba que la función de slicing ([:n]) lance el error 'ValueError'
    si pedimos más películas de las que hay (como lo programamos).
    """
    print("Ejecutando: test_slicing_leer_primeras_n_peliculas_error")
    # 1. PREPARACIÓN
    n = 10 # Pedimos 10, pero en la lista de prueba solo hay 3
    
    # 2. EJECUCIÓN Y VERIFICACIÓN
    # 'pytest.raises' verifica que el código de adentro SÍ lance ese error.
    # Si no lo lanza, la prueba falla.
    with pytest.raises(ValueError):
        peliculasCrud.leerPrimerasNPeliculas(lista_prueba, n)
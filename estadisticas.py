from functools import reduce
import os
from datetime import datetime

#--------------------------------------------------
# FUNCIONES DE ESTADISTICAS (CON DICCIONARIOS)
#--------------------------------------------------

# Función para leer configuración desde un archivo TXT
def leer_configuracion_txt(ruta="config_estadisticas.txt"):
    """
    Lee un archivo de configuración donde se define qué estadísticas ejecutar.
    Ejemplo de archivo:
        DURACION=True
        RESERVAS=False
        EDADES=True
        CATEGORIAS=True
    """
    config = {
        "DURACION": True,
        "RESERVAS": True,
        "EDADES": True,
        "CATEGORIAS": True
    }
    if not os.path.exists(ruta):
        return config

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or "=" not in linea:
                continue
            clave, valor = linea.split("=", 1)
            config[clave.strip().upper()] = valor.strip().lower() == "true"
    return config


# Función para escribir resultados en un archivo TXT
def escribir_resultado_txt(texto, ruta="estadisticas_resultado.txt"):
    """
    Guarda los resultados de las estadísticas en un archivo de texto.
    Se agrega la fecha y hora para tener un registro histórico.
    """
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        f.write(texto + "\n" + "-"*40 + "\n")


def duracion_peliculas(peliculas_lista):
    print("--- Estadísticas de Duración de Películas ---")
    if not peliculas_lista:
        print("No hay datos de películas para calcular estadísticas.")
        return

    duraciones = [p['Duracion_min'] for p in peliculas_lista]
    
    min_duracion = min(duraciones)
    max_duracion = max(duraciones)
    avg_duracion = sum(duraciones) / len(duraciones)
    
    print(f"Duración Mínima: {min_duracion} minutos.")
    print(f"Duración Máxima: {max_duracion} minutos.")
    print(f"Duración Promedio: {avg_duracion:.2f} minutos.")
    print("-" * 40)
    
    # Guardamos el resultado en el TXT
    texto = (
        f"Duración Mínima: {min_duracion} min | "
        f"Máxima: {max_duracion} min | "
        f"Promedio: {avg_duracion:.2f} min"
    )
    escribir_resultado_txt(texto)


def peliculas_mas_reservadas(reservas_lista, funciones_lista, peliculas_lista):
    print("--- Películas Más Reservadas ---")
    if not reservas_lista:
        print("No hay datos de reservas para calcular estadísticas.")
        return

    conteo_peliculas = {}
    for reserva in reservas_lista:
        id_funcion = reserva['ID_Funcion']
        
        funcion_reserva = None
        for f in funciones_lista:
            if f['ID_Funcion'] == id_funcion:
                funcion_reserva = f
                break
        
        if funcion_reserva:
            id_pelicula = funcion_reserva['ID_Pelicula']
            conteo_peliculas[id_pelicula] = conteo_peliculas.get(id_pelicula, 0) + 1

    if not conteo_peliculas:
        print("No se encontraron reservas asociadas a películas.")
        return
        
    peliculas_ordenadas = sorted(conteo_peliculas.items(), key=lambda item: item[1], reverse=True)
    
    print("Ranking de películas por número de reservas:")
    texto = "Ranking de películas por número de reservas:\n"
    for id_pelicula, num_reservas in peliculas_ordenadas:
        pelicula_info = None
        for p in peliculas_lista:
            if p['ID_Pelicula'] == id_pelicula:
                pelicula_info = p
                break
        
        titulo_pelicula = pelicula_info['Titulo'] if pelicula_info else "Desconocido"
        print(f"- '{titulo_pelicula}': {num_reservas} reservas.")
        texto += f"- '{titulo_pelicula}': {num_reservas} reservas.\n"

    print("-" * 40)
    escribir_resultado_txt(texto)#escribe en el txt
    

def analisis_edad_clientes(clientes_lista): 
    print("--- Análisis de Edad de los Clientes ---")

    try:
        if not clientes_lista:
            raise IndexError("La lista de clientes está vacía.")

        edades = []
        for cliente in clientes_lista:
            if 'Edad' not in cliente:
                raise KeyError("Falta la 'Edad' en un cliente.")
            edades.append(cliente['Edad'])

        min_edad = min(edades)
        max_edad = max(edades)
        total_edades = reduce(lambda totalTemp, edad: totalTemp + edad, edades, 0)
        avg_edad = total_edades / len(edades)

        print(f"Edad Mínima de los clientes: {min_edad} años.")
        print(f"Edad Máxima de los clientes: {max_edad} años.")
        print(f"Edad Promedio de los clientes: {avg_edad:.2f} años.")
        
        texto = (
            f"Edad Mínima: {min_edad} | "
            f"Máxima: {max_edad} | "
            f"Promedio: {avg_edad:.2f}"
        )
        escribir_resultado_txt(texto) #escribe en el txt

    except IndexError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    print("-" * 40)


def mostrar_categorias_unicas(peliculas_lista, salas_lista):
    print("\n--- Categorías Únicas Registradas ---")

    texto = "\n--- Categorías Únicas Registradas ---\n"
    if peliculas_lista:
        generos_unicos = set()
        for pelicula in peliculas_lista:
            generos_unicos.add(pelicula['Genero'])
        
        print("Géneros de películas disponibles:")
        texto += "Géneros de películas disponibles:\n"
        for genero in sorted(list(generos_unicos)):
            print(f"- {genero}")
            texto += f"- {genero}\n"

    if salas_lista:
        tipos_sala_unicos = {sala['Tipo'] for sala in salas_lista}
        
        print("\nTipos de salas disponibles:")
        texto += "\nTipos de salas disponibles:\n"
        for tipo in sorted(list(tipos_sala_unicos)):
            print(f"- {tipo}")
            texto += f"- {tipo}\n"
            
    print("-" * 40)

    escribir_resultado_txt(texto) #escribe en el txt


def resumen_clientes_mayores(clientes_lista):
    print("\n--- Clientes Mayores de 30 años ---")
    mayores_30 = list(filter(lambda clientes: clientes['Edad'] > 30, clientes_lista))
    for cliente in mayores_30:
        print(f"{cliente['Nombre']} {cliente['Apellido']} - {cliente['Edad']} años")

    if mayores_30:
        texto = "\nClientes mayores de 30 años:\n" + "\n".join(
            [f"{c['Nombre']} {c['Apellido']} - {c['Edad']} años" for c in mayores_30]
        )
        escribir_resultado_txt(texto) #escribe en el txt


def mostrar_estadisticas(peliculas_lista, clientes_lista, funciones_lista, reservas_lista, salas_lista):
    print("\n--- MENÚ DE ESTADÍSTICAS ---")

    # Se lee el archivo config_estadisticas.txt para decidir qué mostrar
    config = leer_configuracion_txt()

    if config.get("DURACION", True):
        duracion_peliculas(peliculas_lista)
    if config.get("RESERVAS", True):
        peliculas_mas_reservadas(reservas_lista, funciones_lista, peliculas_lista)
    if config.get("EDADES", True):
        analisis_edad_clientes(clientes_lista)
    if config.get("CATEGORIAS", True):
        mostrar_categorias_unicas(peliculas_lista, salas_lista)
    
    print("\n--- Resultados guardados en 'estadisticas_resultado.txt' ---")

from functools import reduce
#--------------------------------------------------
# FUNCIONES DE ESTADISTICAS (CON DICCIONARIOS)
#--------------------------------------------------

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
    for id_pelicula, num_reservas in peliculas_ordenadas:
        pelicula_info = None
        for p in peliculas_lista:
            if p['ID_Pelicula'] == id_pelicula:
                pelicula_info = p
                break
        
        titulo_pelicula = pelicula_info['Titulo'] if pelicula_info else "Desconocido"
        print(f"- '{titulo_pelicula}': {num_reservas} reservas.")
    print("-" * 40)


#falta implementar en menu
def analisis_edad_clientes(clientes_lista): 
    print("--- Análisis de Edad de los Clientes ---")

    try:
        #Forzamos Index error ante lista vacia
        if not clientes_lista:
            raise IndexError("La lista de clientes está vacía.")

        #Forzamos KeyError, si falta alguna 'Edad' en los diccionarios
        edades = []
        for cliente in clientes_lista:
            if 'Edad' not in cliente:
                raise KeyError("Falta la 'Edad' en un cliente.")
            edades.append(cliente['Edad'])

        # Cálculos de estadística
        min_edad = min(edades)
        max_edad = max(edades)
        total_edades = reduce(lambda totalTemp, edad: totalTemp + edad, edades, 0)
        avg_edad = total_edades / len(edades)

        # Resultados
        print(f"Edad Mínima de los clientes: {min_edad} años.")
        print(f"Edad Máxima de los clientes: {max_edad} años.")
        print(f"Edad Promedio de los clientes: {avg_edad:.2f} años.")
    
    except IndexError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    print("-" * 40)

def mostrar_categorias_unicas(peliculas_lista, salas_lista):
    print("\n--- Categorías Únicas Registradas ---")

    if peliculas_lista:
        generos_unicos = set()
        for pelicula in peliculas_lista:
            generos_unicos.add(pelicula['Genero'])
        
        print("Géneros de películas disponibles:")
        for genero in sorted(list(generos_unicos)):
            print(f"- {genero}")

    if salas_lista:
        tipos_sala_unicos = {sala['Tipo'] for sala in salas_lista}
        
        print("\nTipos de salas disponibles:")
        for tipo in sorted(list(tipos_sala_unicos)):
            print(f"- {tipo}")
            
    print("-" * 40)
#falta implementar en menu
def resumen_clientes_mayores(clientes_lista):
    print("\n--- Clientes Mayores de 30 años ---")
    mayores_30 = list(filter(lambda clientes: clientes['Edad'] > 30, clientes_lista)) #USO DE FILTER PARA OBTENER CLIENTES MAYORES A 30 AÑOS
    for cliente in mayores_30:
        print(f"{cliente['Nombre']} {cliente['Apellido']} - {cliente['Edad']} años")

def mostrar_estadisticas(peliculas_lista, clientes_lista, funciones_lista, reservas_lista, salas_lista):
    print("\n--- MENÚ DE ESTADÍSTICAS ---")
    duracion_peliculas(peliculas_lista)
    peliculas_mas_reservadas(reservas_lista, funciones_lista, peliculas_lista)
    analisis_edad_clientes(clientes_lista)
    mostrar_categorias_unicas(peliculas_lista, salas_lista)
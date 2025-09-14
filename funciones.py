# Función para imprimir listas de diccionarios 
def imprimir_lista_diccionarios(titulo, lista_de_diccionarios):
    print(f"\n--- {titulo.upper()} ---")

    if not lista_de_diccionarios:
        print("La lista está vacía.")
        return

    headers = list(lista_de_diccionarios[0].keys())
    
    col_widths = {key: len(key) for key in headers}
    for item in lista_de_diccionarios:
        for key, value in item.items():
            if len(str(value)) > col_widths[key]:
                col_widths[key] = len(str(value))

    header_line = " | ".join([header.ljust(col_widths[header]) for header in headers])
    print(header_line)
    print("-" * len(header_line))

    for item in lista_de_diccionarios:
        row_line = " | ".join([str(item.get(header, "")).ljust(col_widths[header]) for header in headers])
        print(row_line)

    print("-" * len(header_line))
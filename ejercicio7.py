def guardar_transformacion(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:
        resultado = "opción inválida"
    
    with open("resultado.txt", "w") as archivo:
        archivo.write(resultado)
    
    return resultado 
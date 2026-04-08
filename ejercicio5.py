def transformar_con_validacion(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "opción inválida"
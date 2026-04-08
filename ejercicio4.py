def transformar_lista(lista_palabras, numero):
    nueva_lista = []
    if numero == 1:
        for palabra in lista_palabras:
            nueva_lista.append(palabra.upper())
    elif numero == 2:
        for palabra in lista_palabras:
            nueva_lista.append(palabra.lower())
    elif numero == 3:
        for palabra in lista_palabras:
            nueva_lista.append(palabra.capitalize())
    return nueva_lista 
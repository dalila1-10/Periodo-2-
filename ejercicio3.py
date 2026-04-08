def transformar_texto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()

# Pedir datos al usuario
texto_usuario = input("Ingrese un texto: ")
numero_usuario = int(input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): "))

# Llamar a la función y mostrar el resultado
resultado = transformar_texto(texto_usuario, numero_usuario)
print("Resultado:", resultado)
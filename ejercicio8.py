def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"

print("=" * 40)
print("       PROGRAMA DE TRANSFORMACIÓN")
print("=" * 40)
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en mayúscula")
print("=" * 40)

texto_usuario = input("Ingrese el texto: ")

try:
    opcion_usuario = int(input("Elija una opción (1, 2 o 3): "))
    resultado = transformar(texto_usuario, opcion_usuario)
    print("\n" + "=" * 40)
    print("RESULTADO:", resultado)
    print("=" * 40)
except ValueError:
    print("Error: Debe ingresar un número válido.")
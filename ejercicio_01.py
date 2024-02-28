# Ejercicio 01
def escribir_centrado(texto):
    # Calculamos el número de espacios necesarios para centrar el texto
    num_espacios = (80 - len(texto)) // 2
    # Imprimimos los espacios seguidos del texto
    print(' ' * num_espacios + texto)
    # Subrayamos el texto con el carácter '='
    print(' ' * num_espacios + '=' * len(texto))


# Prueba de la función
escribir_centrado("Hola Mundo")

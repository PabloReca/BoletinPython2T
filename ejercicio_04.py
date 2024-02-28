# Ejercicio 04
def convertir_espaciado(texto):
    # Añadimos un espacio después de cada carácter
    texto_espaciado = " ".join(texto)
    return texto_espaciado


def main():
    texto = input("Introduce un texto: ")
    texto_espaciado = convertir_espaciado(texto)
    print(f"Texto con espaciado: {texto_espaciado}")


if __name__ == "__main__":
    main()

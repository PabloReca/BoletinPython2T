# Ejercicio 05
def calcular_max_min(lista_numeros):
    return max(lista_numeros), min(lista_numeros)


def main():
    numeros = []
    while True:
        numero = input("Introduce un número (o escribe 'salir' para terminar): ")
        if numero.lower() == 'salir':
            break
        else:
            numeros.append(float(numero))

    if numeros:
        maximo, minimo = calcular_max_min(numeros)
        print(f"El valor máximo es: {maximo}, y el mínimo es: {minimo}")
    else:
        print("No se introdujeron números.")


if __name__ == "__main__":
    main()

# Ejercicio 08
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    numero = int(input("Introduce un número entero para calcular su factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")


if __name__ == "__main__":
    main()

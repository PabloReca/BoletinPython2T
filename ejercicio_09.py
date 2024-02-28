# Ejercicio 09
def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    mcd = calcular_mcd(num1, num2)
    print(f"El MCD de {num1} y {num2} es {mcd}")


if __name__ == "__main__":
    main()

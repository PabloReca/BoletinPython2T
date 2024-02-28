# Ejercicio 02
def es_multiplo(num1, num2):
    # Comprobamos si num1 es múltiplo de num2
    return num1 % num2 == 0 or num2 % num1 == 0


# Programa que pide dos números y muestra si uno es múltiplo del otro
def main():
    # Pedimos al usuario que introduzca dos números enteros
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))

    # Llamamos a la función EsMultiplo y mostramos el resultado
    if es_multiplo(num1, num2):
        print("Uno de los números es múltiplo del otro.")
    else:
        print("Ninguno de los números es múltiplo del otro.")


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

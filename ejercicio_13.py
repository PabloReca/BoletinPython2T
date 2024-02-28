# Ejercicio 13

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplificar_fraccion(numerador, denominador):
    divisor = mcd(numerador, denominador)
    return numerador // divisor, denominador // divisor


def leer_fraccion():
    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    return simplificar_fraccion(numerador, denominador)


def escribir_fraccion(numerador, denominador):
    if denominador == 1:
        print(numerador)
    else:
        print(f"{numerador}/{denominador}")


def operar_fracciones(operacion):
    n1, d1 = leer_fraccion()
    n2, d2 = leer_fraccion()
    if operacion == "sumar":
        resultado = simplificar_fraccion(n1 * d2 + n2 * d1, d1 * d2)
    elif operacion == "restar":
        resultado = simplificar_fraccion(n1 * d2 - n2 * d1, d1 * d2)
    elif operacion == "multiplicar":
        resultado = simplificar_fraccion(n1 * n2, d1 * d2)
    elif operacion == "dividir":
        resultado = simplificar_fraccion(n1 * d2, n2 * d1)
    escribir_fraccion(*resultado)


def main():
    while True:
        print("\n1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            operar_fracciones("sumar")
        elif opcion == "2":
            operar_fracciones("restar")
        elif opcion == "3":
            operar_fracciones("multiplicar")
        elif opcion == "4":
            operar_fracciones("dividir")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

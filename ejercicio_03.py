# Ejercicio 03
def calcular_temperatura_media(maxima, minima):
    return (maxima + minima) / 2


def main():
    numero_dias = int(input("¿Cuántos días vas a introducir? "))
    for _ in range(numero_dias):
        maxima = float(input("Introduce la temperatura máxima del día: "))
        minima = float(input("Introduce la temperatura mínima del día: "))
        media = calcular_temperatura_media(maxima, minima)
        print(f"La temperatura media del día es: {media} grados Celsius.")


if __name__ == "__main__":
    main()

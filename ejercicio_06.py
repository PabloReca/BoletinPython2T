# Ejercicio 06
import math


def calcular_area_perimetro_circunferencia(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro


def main():
    radio = float(input("Introduce el radio de la circunferencia: "))
    area, perimetro = calcular_area_perimetro_circunferencia(radio)
    print(f"Área de la circunferencia: {area:.2f}, Perímetro de la circunferencia: {perimetro:.2f}")


if __name__ == "__main__":
    main()

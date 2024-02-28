# Ejercicio 10

def segundos_a_hms(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60
    return horas, minutos, segundos


def hms_a_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos


def main():
    while True:
        print("\n1. Convertir a segundos")
        print("2. Convertir a horas, minutos y segundos")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            horas = int(input("Horas: "))
            minutos = int(input("Minutos: "))
            segundos = int(input("Segundos: "))
            total_segundos = hms_a_segundos(horas, minutos, segundos)
            print(f"Total: {total_segundos} segundos")
        elif opcion == "2":
            segundos = int(input("Segundos: "))
            horas, minutos, segundos = segundos_a_hms(segundos)
            print(f"Total: {horas}h {minutos}m {segundos}s")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

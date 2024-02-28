# Ejercicio 12
from ejercicio_11 import dias_del_mes, calcular_dia_juliano


def leer_fecha():
    while True:
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        ano = int(input("Año: "))
        if validar_fecha(dia, mes, ano):
            break
        else:
            print("Fecha inválida, por favor ingrese nuevamente.")
    return dia, mes, ano


def validar_fecha(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_del_mes(mes, ano):
        return False
    return True


# Las funciones DiasDelMes, EsBisiesto, y Calcular_Dia_Juliano se mantienen iguales

def main():
    print("Introduce una fecha válida para calcular su día juliano:")
    dia, mes, ano = leer_fecha()
    dia_juliano = calcular_dia_juliano(dia, mes, ano)
    print(f"El día juliano es: {dia_juliano}")


if __name__ == "__main__":
    main()

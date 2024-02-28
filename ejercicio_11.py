# Ejercicio 11

def leer_fecha():
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    ano = int(input("Año: "))
    return dia, mes, ano


def dias_del_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if mes in [4, 6, 9, 11]:
        return 30
    if mes == 2:
        return 29 if es_bisiesto(ano) else 28


def es_bisiesto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def calcular_dia_juliano(dia, mes, ano):
    total_dias = sum(dias_del_mes(m, ano) for m in range(1, mes)) + dia
    return total_dias


def main():
    print("Introduce una fecha para calcular su día juliano:")
    dia, mes, ano = leer_fecha()
    dia_juliano = calcular_dia_juliano(dia, mes, ano)
    print(f"El día juliano es: {dia_juliano}")


if __name__ == "__main__":
    main()

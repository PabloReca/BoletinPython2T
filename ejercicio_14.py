# Ejercicio 14

def longitud_pila(pila):
    return len(pila)


def esta_vacia_pila(pila):
    return len(pila) == 0


def esta_llena_pila(pila, capacidad=10):  # Asumimos una capacidad máxima para la pila
    return len(pila) >= capacidad


def add_pila(cadena, pila):
    if esta_llena_pila(pila):
        print("Error: La pila está llena.")
    else:
        pila.append(cadena)


def sacar_de_la_pila(pila):
    if esta_vacia_pila(pila):
        print("Error: La pila está vacía.")
    else:
        return pila.pop()


def escribir_pila(pila):
    print("Elementos de la pila:")
    for elemento in reversed(pila):
        print(elemento)


def main_pila():
    pila = []
    while True:
        print("\n1. Añadir elemento a la pila")
        print("2. Sacar elemento de la pila")
        print("3. Longitud de la pila")
        print("4. Mostrar pila")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            cadena = input("Introduce el elemento a añadir: ")
            add_pila(cadena, pila)
        elif opcion == "2":
            elemento = sacar_de_la_pila(pila)
            if elemento is not None:
                print(f"Elemento sacado: {elemento}")
        elif opcion == "3":
            print(f"Longitud de la pila: {longitud_pila(pila)}")
        elif opcion == "4":
            escribir_pila(pila)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main_pila()

# Ejercicio 15
from ejercicio_14 import esta_vacia_pila, escribir_pila, longitud_pila, add_pila


# Reutilizamos las funciones del ejercicio 14, excepto SacarDeLaPila, que se convierte en SacarDeLaCola

def sacar_de_la_cola(cola):
    if esta_vacia_pila(cola):  # Reutilizamos EstaVaciaPila ya que la lógica es la misma
        print("Error: La cola está vacía.")
    else:
        return cola.pop(0)


def main_cola():
    cola = []
    while True:
        print("\n1. Añadir elemento a la cola")
        print("2. Sacar elemento de la cola")
        print("3. Longitud de la cola")
        print("4. Mostrar cola")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            cadena = input("Introduce el elemento a añadir: ")
            add_pila(cadena, cola)  # Reutilizamos AddPila ya que la lógica de adición es la misma
        elif opcion == "2":
            elemento = sacar_de_la_cola(cola)
            if elemento is not None:
                print(f"Elemento sacado: {elemento}")
        elif opcion == "3":
            print(f"Longitud de la cola: {longitud_pila(cola)}")  # Reutilizamos LongitudPila por la misma lógica
        elif opcion == "4":
            escribir_pila(cola)  # Reutilizamos EscribirPila aunque ahora es una cola
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main_cola()

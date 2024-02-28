# Ejercicio 07
def login(usuario, contrasena, intentos):
    if usuario == "usuario1" and contrasena == "asdasd":
        return True, intentos
    else:
        intentos += 1
        return False, intentos


def main():
    intentos = 0
    while intentos < 3:
        usuario = input("Introduce el nombre de usuario: ")
        contrasena = input("Introduce la contraseña: ")
        exito, intentos = login(usuario, contrasena, intentos)
        if exito:
            print("Login exitoso.")
            break
        else:
            print(f"Login fallido. Intentos restantes: {3 - intentos}")
    if intentos == 3:
        print("Se han superado los intentos permitidos.")


if __name__ == "__main__":
    main()

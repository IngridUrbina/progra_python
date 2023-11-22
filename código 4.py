import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Dar la bienvenida al usuario
print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100.")

# Inicializar variables
intentos = 0
max_intentos = 5

# Bucle principal del juego
while intentos < max_intentos:
    # Pedir al usuario que ingrese un número
    intento_usuario = int(input("Intenta adivinar el número: "))

    # Incrementar el contador de intentos
    intentos += 1

    # Comparar el número ingresado con el número secreto
    if intento_usuario == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
    elif intento_usuario < numero_secreto:
        print("El número es mayor. ¡Sigue intentando!")
    else:
        print("El número es menor. ¡Sigue intentando!")

# Mostrar el número secreto si el usuario no adivina
if intentos == max_intentos:
    print(f"¡Agotaste tus {max_intentos} intentos! El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")

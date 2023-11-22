# Crear una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar los números pares
numeros_pares = [num for num in numeros if num % 2 == 0]

# Elevar al cuadrado cada número par
cuadrados_pares = [num ** 2 for num in numeros_pares]

# Imprimir los resultados
print("Lista original:", numeros)
print("Números pares:", numeros_pares)
print("Cuadrados de números pares:", cuadrados_pares)

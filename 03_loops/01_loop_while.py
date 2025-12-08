###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 1
while contador <= 10:
    print(contador)
    contador +=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero = 1
suma_pares = 0
while numero <= 20:
    if numero % 2 == 0:
        suma_pares += numero
    numero += 1
print(f"La suma de los numeros pares hasta el 20 es: {suma_pares}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduce un numero positivo: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print(f"El factorial de {numero} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contraseña = ""
while len(contraseña) < 8:
    contraseña = input("Introduce una contraseña de al menos 8 carecteres: ")
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 carecteres. INtentalo de nuevo")
print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

multiplicado = int(input("Introduce número: "))
multiplicador = 1

while multiplicador <= 10:
    resultado = multiplicado * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce número positivo: "))
numero = 2

while numero <= n:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)
    numero += 1
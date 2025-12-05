###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = int(input("Añade el primer núemero: "))
num2 = int(input("Añade el segundo número: "))
if num1 > num2:
  print(f"{num1} es más grande que {num2}")
elif num2 > num1:
  print(f"{num1} es más pequeño que {num2}")
else:
  print("Son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operación = input("Introduce la operación (+, -, *, /): ")
if operación == "+":
  resultado = num1 + num2
elif operación == "-":
  resultado = num1 - num2
elif operación == "*":
  resultado = num1 * num2
elif operación == "/":
  if num2 == "0":
    print("ERROR: No se puede dividir entre 0 bobo!!")
  else:
    resultado = num1 / num2
else:
  print("Operación no valida")

if 'resultado' in locals():
  print(f"El resultado es: {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


año = int(input("Introduce año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
  print(f"{año} es un año bisiesto")
else:
  print(f"{año} no es un año bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

import os
os.system("clear")

edad = int(input("¿Qué edad tienes?: "))
if 0 <= edad <= 2:
  print("Bebe")
elif 3 <= edad <= 12:
  print("Niñ@")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= 65:
  print("Adulto mayor")
elif edad >= 110:
  print("¿Como sigues vivo?")
else:
  print("No existes")
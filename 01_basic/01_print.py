# El módulo print() es el módulo que nos permite imprimir en consola
print("¡Hola, mundo!")
print('También funciona con una sola comilla')

print("Python", "es", "marvilloso")
# Podemos importar módulos de Python para usarlos en nuestros programas.
# En este caso, importamos el módulo "os" que nos da acceso a funciones
# relacionadas con el sistema operativo
from os import system

# system() nos permite ejecutar un comando en la terminal.
# En este caso, lo hacemos para limpiar la pantalla tanto
# en MacOS/Linux usando "clear" como en Windows con "cls"
if system("cls") != 0: system
"""
Crear un programa que pida dos números enteros y obtenga como resultado cual de ellos
es par o si ambos lo son
"""

entrada = int(input("Ingrese el primer numero: "))
entrada2 = int(input("Ingrese el segundo numero: "))
if entrada % 2 == 0 and entrada2 % 2 == 0:
    print("Ambos numeros son pares")
elif entrada % 2 == 0:
    print(f"El primer numero {entrada} es par y el segundo numero {entrada2} es impar")


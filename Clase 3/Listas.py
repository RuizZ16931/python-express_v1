"""
Ejemplos de listas en Python
"""

array = ["futbol", "baloncesto", 18.6, 18, [6,7,10.4] ,True, False ,"natacion"]

print(array) 

# Acceso a elementos de la lista
print(array[0])  # Imprime el primer elemento de la lista
print(array[1])  # Imprime el segundo elemento de la lista
print(array[0:3]) # Imprime los primeros tres elementos de la lista
print(len(array))  # Imprime la longitud de la lista
array.append("voleibol")  # Agrega un nuevo elemento al final de la list
print(array)  # Imprime la lista actualizada
array.insert(2, "tenis")  # Inserta un nuevo elemento en la posición 2
print(array)  # Imprime la lista actualizada
array.extend(["golf", "boxeo"])  # Agrega múltiples elementos al final de la lista
print(array)  # Imprime la lista actualizada
array.remove("baloncesto")  # Elimina el primer elemento con el valor "baloncesto"
print(array)  # Imprime la lista actualizada
array.pop()  # Elimina el último elemento de la lista
print(array)  # Imprime la lista actualizada
array.pop(2)  # Elimina el elemento en la posición 2
print(array)  # Imprime la lista actualizada
array.clear()  # Elimina todos los elementos de la lista
print(array)  # Imprime la lista actualizada, que ahora está vacía

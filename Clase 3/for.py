"""
Ejemplo de estructuras de control for en Python.
"""
# Ejemplo en C
# for (int i = 0; i < 10; i++) {
#     cout << "El valor de i es: " << i << endl;
# }

#contador = 10
#for i in range(contador): 
  #print("El valor de i es:", i) # Imprime los valores de 0 a 9
  #print("Fin del bucle for") #Mensaje al final de cada iteracion

# Ejemplo de iteracion sobre una lista
array = ["Python", "Java", "C++", "True", "10.5", "100"]
print(len(array))  # Imprime la longitud de la lista
array.append("JavaScript")  # Agrega un nuevo elemento a la lista
print(array)
for i in range(len(array)):  # Itera sobre los índices de la lista
    print("El valor de la posicion es:", array[i])  # Imprime el índice y el valor de la lista
print("Fin del bucle for")


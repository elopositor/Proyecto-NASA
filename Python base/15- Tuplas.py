# Tupla es igual que una lista, pero no se puede modificar
# Se usan cuando queramos modificar accidentalmente una lista

# Se definen con parentesis
numeros = (1, 2, 3) + (4, 5, 6)
punto = tuple([1, 2])  # Tambien se puede transformar una lista en tupla así

numeros[1] = 5  # No se puede moddificar. Error

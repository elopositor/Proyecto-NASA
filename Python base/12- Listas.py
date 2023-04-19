# Listas
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
booleans = [True, False, True]
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
repetir = [0] * 10
repetir01 = [0, 1] * 10

bindListas = numeros + letras
rango = list(range(1, 11, 1))  # Lista lee un iterable
chars = list("Hola mundo")

# Manipulacion de listas
mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
mascotas[0:2]
mascotas[-1]  # ültimo indice (da la vuelta)
mascotas[0::3]  # Saltando 3

# Desempaquetar listas
numeros = [1, 2, 3]

# Feo
primero = numeros[0]
primero = numeros[1]
primero = numeros[2]

primero, segundo, tercero = numeros
primero, *otros = numeros
*otros, ultimo = numeros

# Iterar listas
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

# Sin indice
for mascota in mascotas:
    print(mascota)

# Tupla: usando funcion enumerate
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)

# Buscar elementos. En python da error si no existe
if "Pulga" in mascotas:
    mascotas.index("Pulga")

# Insertar y eliminar elementos
mascotas = [
    "Pelusa",
    "Pulga",
    "Felipe",
    "Chanchito Feliz"]

mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # Agregar al final
mascotas.remove("Pulga")  # Eliminar por nombre. SOLO ELEMINA EL PRIMERO
mascotas.pop(1)  # Elimina por indice
del mascotas[0]  # Elimina por indice también
mascotas.clear  # Elimina todos los elementos


# Ordenar listas
numeros = [2, 1, 50, 30, 21]
numeros.sort()  # Ordena de menor a mayor
numeros.sort(reverse=True)
sorted(numeros)  # Para asignar a nueva variable

usuarios = [[4, "Chanchito"], [1, "Felipe"],
            [5, "Pulga"]]
usuarios.sort()  # Ordena por el primer elemento

# Creamos funcion que devuelva el primer elemento


def ordena(nombre):
    return (nombre[1])


usuarios.sort(key=ordena)  # Así ordenamos por el segundo elemento

usuarios = [[4, "Chanchito"], [1, "Felipe"],
            [5, "Pulga"], [2, "Ana"]]

# Seleccionar solo segundo elemento
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# Filtrar
nombres = [usuario for usuario in usuarios if usuario[0] > 1]

# Filtrar y transformar
nombres = [usuario[1] for usuario in usuarios if usuario[0] > 1]

# map y filter
nombres = list(map(
    lambda usuario: usuario[0],
    usuarios
))

nombres = list(filter(
    lambda usuario: usuario[0] > 1,
    usuarios
))

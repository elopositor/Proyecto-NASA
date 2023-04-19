
# Iteración
for numero in range(5):
    print("Hola mundo" * numero)

# Detener iteración con break
# Incluir else en el for: si no hace break, va a pasar por ahí
buscar = 11
for i in range(10):
    print(i)
    if buscar == i:
        print("encontrado", buscar)
        break
else:
    print("no encontrado el número buscado")

# Caracteres: imprimer cada uno de los caracteres
for char in "Hola mundo":
    print(char)

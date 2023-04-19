def hola(nombre="", apellido=""):
    print(f"Hola {nombre} {apellido}")


hola("Alberto")

# xargs: para pasar multiples argumentos, sin saber cuantos se van a recibir


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)

# kargs: keywords arguments -> para empaquetar todos los parámetros en uno solo


def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")

# return las funciones


def suma(a, b):
    resultado = a + b
    return resultado


b = suma(2, 3)
print(b)

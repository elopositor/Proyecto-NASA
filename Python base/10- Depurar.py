# Depurar: Nos vamos a la pestaña de depurar (izquierda)
# Ponemos breakpoint
def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


# print("chanchito")
l = largo("Hola mundo")
print(l)

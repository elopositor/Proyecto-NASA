# Checkear si es palindromo
def es_palindromo(texto):
    texto = texto.lower()
    texto = no_space(texto)

    revert = ""
    for i in range(len(texto), 0, -1):
        revert += texto[i-1]
    isPalin = True if revert == texto else False
    return (print(f"{texto}: {isPalin}"))

# Quitar espacios


def no_space(texto):
    textoSE = ""
    for i in texto:
        i = i if i != " " else ""
        textoSE += i
    return textoSE


es_palindromo("Amo la paloma")

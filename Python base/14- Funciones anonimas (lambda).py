# lambda parametros:valorRetorno
usuarios = [[4, "Chanchito"], [1, "Felipe"],
            [5, "Pulga"], [2, "Ana"]]

usuarios.sort(key=lambda usuario: usuario[1])  # Ordena por el primer elemento
print(usuarios)

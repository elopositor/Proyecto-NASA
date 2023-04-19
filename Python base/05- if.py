edad = 60
sexo = "mujer"

# Todo lo que esté anidado dentro del if es lo que ejecuta como if
if edad > 54 and sexo == "hombre":
    print("Puede ver la película con descuento de hombre")
elif edad > 54 and sexo == "mujer":
    print("Puede ver la película con descuento de mujer")
elif edad > 17:
    print("Puede ver la película")
else:
    print("No puede ver la película")

# Operador ternario
mensaje = "Es mayor" if edad > 18 else "Es menor"
print(mensaje)

# and, or, not (son operaciones de cortocircuito)
mensaje = "Es mayor" if not edad > 18 else "Es menor"
print(mensaje)

mensaje = "Es mayor o mujer" if edad > 18 or sexo == "mujer" else "Es menor"
print(mensaje)

# Encadenar operaciones de comparación
edad = 18
if 15 <= edad <= 65:
    print("puede entrar en la piscina")

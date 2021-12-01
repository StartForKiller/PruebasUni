texto = "Esto es una prueba"
fecha = "16/10/2000"

print(len(texto))

resultado = fecha + " - " + texto

print(resultado)

print("esto" in texto)
print("prueba" in texto)

print(texto.split())
print(texto.split("e"))

print(fecha.split("/"))

help(str.replace)
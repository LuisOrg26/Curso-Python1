Signo = [" ",",","."]
frase = "Hola, hoy estoy aprendiendo Python. Feliz Domingo."
espacios_encontrados = 0
comas_encontradas = 0
puntos_encontrados = 0

for letra in frase:
    if letra in Signo:
        if letra == " ":
            print("Se ha encontrado un espacio\n")
            espacios_encontrados += 1
        if letra == ",":
            print("Se ha encontrado una coma\n")
            comas_encontradas += 1
        if letra == ".":
            print("Se ha encontrado un punto\n")
            puntos_encontrados += 1

print("Se ha encontrado un total de {} espacios, {} comas, {} puntos".format(espacios_encontrados,comas_encontradas,puntos_encontrados))

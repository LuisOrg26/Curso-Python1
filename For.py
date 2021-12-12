Signo = [" ",",","."]

espacios_encontrados = 0
comas_encontradas = 0
puntos_encontrados = 0
frase = str(input("Introduzca una frase"))
for letra in frase:
    if letra in Signo:
        if letra == " ":
            espacios_encontrados += 1
        if letra == ",":
            comas_encontradas += 1
        if letra == ".":
            puntos_encontrados += 1

print("Se ha encontrado un total de {} espacios, {} comas, {} puntos".format(espacios_encontrados,comas_encontradas,puntos_encontrados))

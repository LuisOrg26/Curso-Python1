Vocales = ["a","e","i","o","u"]
frase = "Hola, hoy estoy aprendiendo Python"
vocales_encontradas = 0

for letra in frase:
    if letra in Vocales:
        vocales_encontradas += 1


print(vocales_encontradas)
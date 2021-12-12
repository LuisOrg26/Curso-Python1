numeros = []
añadir = "S"


numeros_introducidos = input("Introduzca los numero separados por comas: ")
numeros = [int(i) for i in numeros_introducidos.split(",")]
print(numeros)
numero_mayor = numeros[0]
numero_menor = numeros[0]
for numero in numeros[1:]:
    if numero_menor > numero:
        numero_menor = numero
    if numero_mayor < numero:
        numero_mayor = numero

print("El numero más pequeño es: {}\n"
      "Y el numero más grande es: {}".format(numero_menor,numero_mayor))

def potencia(numero,num_potencia=2):
    poten = numero
    for i in range(num_potencia-1):
        poten *= numero
    return poten



if __name__ == "__main__":
    select =input("¿Quiere sacar potencia de dos o un numero mayor?\n"
                    "S = dos\n"
                    "N = mayor\n")
    if select == "S":
        numero = int(input("Digame un numero para sacarle potencia "))
        potenciado = potencia(numero)
    if select == "N":
        numero = int(input("Digame un numero para sacarle potencia "))
        potenci = int(input("Digame cual es el exponente "))
        potenciado = potencia(numero,num_potencia=potenci)
    print("La potencia del numero {} es {}".format(numero,potenciado))

def potencia(numero):
    pote = numero * numero
    return pote



if __name__ == "__main__":
    numero = int(input("Digame un numero para sacarle potencia"))
    potenciado = potencia(numero)
    print("La potencia del numero {} es {}".format(numero,potenciado))
from random import randint

def guess(word):
    know = False
    while know == False:
        number = int(input("¿Cual es el numero?"))
        if number == word:
            print("Felicidades encontraste el numero")
            know = True
        else:
            print("Vuelvalo a intentar")



if __name__ == "__main__":
    numero = randint(1,100)
    guess(numero)
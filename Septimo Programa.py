#Combate pokemon
from random import randint
import os
vida_pika = 80
vida_squirt = 80
vida_total_pika = 80
vida_total_squirt = 80
CANTIDAD_DE_BARRA = 10
Titulo = ("Combate Pokemon")
print(Titulo, "\n"+"-"*len(Titulo)+"\n")
while vida_pika > 0 or vida_squirt > 0:
    print("Turno de Pikachu")
    ataque_pika = randint(1,2)
    if ataque_pika == 1:
        print("Ataque de Bola voltio")
        vida_squirt -= 10
    else:
        print("Ataque de Onda Trueno")
        vida_squirt -= 11

    if vida_squirt < 0:
        vida_squirt = 0
    if vida_pika < 0:
        vida_pika = 0
    valor_squirt = int(vida_squirt)*CANTIDAD_DE_BARRA/vida_total_squirt
    valor_pika = int(vida_pika)*CANTIDAD_DE_BARRA/vida_total_pika
    barra_pika = ("["+"⬛"*(int(valor_pika))+"-"*(int(CANTIDAD_DE_BARRA-valor_pika))+"]")
    barra_squirt = ("["+"⬛"*(int(valor_squirt))+"-"*(int(CANTIDAD_DE_BARRA-valor_squirt))+"]")
    print("Pikachu:   {} {}\n"
          "Squirtle:   {} {}\n".format(barra_pika,vida_pika,barra_squirt,vida_squirt))
    input("Enter para continuar...\n\n")
    os.system("cls")
    print("Turno de Squirtle")
    ataque_squirt = None
    while ataque_squirt != "P" and ataque_squirt != "A" and ataque_squirt != "B" and ataque_squirt != "N":
        ataque_squirt = input("¿Que ataque deseas hacer?\n"
                              "P = Placaje\n"
                              "A = Pistola de agua\n"
                              "B = Burbuja\n"
                              "N = Nada\n")

    if ataque_squirt == "P":
        print("Squirtle ataca con placaje")
        vida_pika -= 10
    elif ataque_squirt == "A":
        print("Squirtle ataca con Pistola de Agua")
        vida_pika -= 12
    elif ataque_squirt == "B":
        print("Suirtle ataca con Burbuja")
        vida_pika -= 9
    elif ataque_squirt == "N":
        print("Squirtle no ataca")

    if vida_squirt < 0:
        vida_squirt = 0
    if vida_pika < 0:
        vida_pika = 0
    valor_squirt = int(vida_squirt)*CANTIDAD_DE_BARRA/vida_total_squirt
    valor_pika = int(vida_pika)*CANTIDAD_DE_BARRA/vida_total_pika
    barra_pika = ("["+"⬛"*(int(valor_pika))+"-"*(int(CANTIDAD_DE_BARRA-valor_pika))+"]")
    barra_squirt = ("["+"⬛"*(int(valor_squirt))+"-"*(int(CANTIDAD_DE_BARRA-valor_squirt))+"]")
    print("Pikachu:   {} Vida: {}\n"
          "Squirtle:   {} Vida: {}\n".format(barra_pika,vida_pika,barra_squirt,vida_squirt))

    input("Enter para continuar...\n\n")
    os.system("cls")
if vida_squirt <= 0:
    print("Squirtle Pierde el ganador es Pikachu con {} de vida".format(vida_pika))
else:
    print("Pikachu Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
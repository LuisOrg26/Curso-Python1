#Combate pokemon
from random import randint
import os
vida_pika = 80
vida_squirt = 80
vida_total_pika = 80
vida_total_squirt = 80
Titulo = ("Combate Pokemon")
print(Titulo, "\n"+"-"*len(Titulo)+"\n")
while vida_pika > 0 and vida_squirt > 0:
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
    barra_pika = ("["+"⬛"*(vida_pika)+"-"*(vida_total_pika-vida_pika)+"]")
    barra_squirt = ("["+"⬛"*(vida_squirt)+"-"*(vida_total_squirt-vida_squirt)+"]")
    print("Pikachu:   {} {}\n"
          "Squirtle:   {} {}\n".format(barra_pika,vida_pika,barra_squirt,vida_squirt))
    input("Enter para continuar...\n\n")
    os.system("cls")
    print("Turno de Squirtle")
    ataque_squirt = None
    while ataque_squirt != "P" and ataque_squirt != "A" and ataque_squirt != "B":
        ataque_squirt = input("¿Que ataque deseas hacer?\n"
                              "P = Placaje\n"
                              "A = Pistola de agua\n"
                              "B = Burbuja\n")

    if ataque_squirt == "P":
        print("Squirtle ataca con placaje")
        vida_pika -= 10
    elif ataque_squirt == "A":
        print("Squirtle ataca con Pistola de Agua")
        vida_pika -= 12
    elif ataque_squirt == "B":
        print("Suirtle ataca con Burbuja")
        vida_pika -= 9

    if vida_squirt < 0:
        vida_squirt = 0
    if vida_pika < 0:
        vida_pika = 0
    barra_pika = ("["+"⬛"*(vida_pika)+"-"*(vida_total_pika-vida_pika)+"]")
    barra_squirt = ("["+"⬛"*(vida_squirt)+"-"*(vida_total_squirt-vida_squirt)+"]")
    print("La vida de Pikachu es de {}\n"
          "La vida de Squirtle es de {}\n".format(barra_pika,barra_squirt))

    input("Enter para continuar...\n\n")
    os.system("cls")
if vida_squirt <= 0:
    print("Squirtle Pierde el ganador es Pikachu con {} de vida".format(vida_pika))
else:
    print("Pikachu Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
import os
import readchar
import random
from random import randint
POS_X = 0
POS_Y = 1
enemy_life = 0
vida_pika = 80
vida_squirt = 80
vida_bulbasour = 100
vida_charman = 70
vida_mewtwo = 80
vida_total_mewtwo = 80
vida_total_charman= 70
vida_total_bulbasour = 100
vida_total_pika = 80
vida_total_squirt = 80
CANTIDAD_DE_BARRA = 10
POKE_TRAINERS = 4
map_trainers = []
my_position = [2,1]
obstacle_definition = """▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓  ▓▓▓▓▓▓▓    ▓▓▓▓▓▓
▓                ▓▓▓
▓▓                ▓▓
▓▓               ▓▓▓
▓▓               ▓▓▓
▓▓▓▓        ▓▓▓  ▓▓▓
▓▓▓▓         ▓▓   ▓▓
▓▓▓          ▓▓     
▓▓             ▓▓   
▓▓     ▓▓▓▓    ▓▓   
▓▓    ▓▓▓▓▓▓▓   ▓▓  
▓               ▓▓  
      ▓▓▓▓▓▓    ▓▓  """
end_game = False
poke_battle = False
poke_explore = True
died = False
exit = False
obstacle_in_object = False
obstacles_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacles_definition[0])
MAP_HEIGHT = len(obstacles_definition)
for i in range(POKE_TRAINERS):
    x = random.randint(0, MAP_WIDTH-1)
    y = random.randint(0, MAP_HEIGHT-1)
    while obstacles_definition[y][x]!= " ":
        x = random.randint(0, MAP_WIDTH-1)
        y = random.randint(0, MAP_HEIGHT-1)
    else:
        map_trainers.append([x,y])
titulo = "▓▓▓▓    ▓▓▓▓▓   ▓   ▓   ▓▓▓▓▓           ▓▓▓▓▓   ▓▓▓▓▓   ▓       ▓▓▓▓▓     ▓  \n" \
         "▓   ▓   ▓   ▓   ▓  ▓    ▓               ▓    ▓  ▓       ▓       ▓        ▓ ▓ \n" \
         "▓   ▓   ▓   ▓   ▓ ▓     ▓▓▓             ▓    ▓  ▓▓▓     ▓       ▓▓▓     ▓   ▓\n" \
         "▓▓▓▓    ▓   ▓   ▓ ▓     ▓               ▓▓▓▓▓   ▓       ▓       ▓       ▓▓▓▓▓\n" \
         "▓       ▓▓▓▓▓   ▓  ▓    ▓▓▓▓▓           ▓       ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓   ▓"

pelea =  "▓▓▓▓▓   ▓▓▓▓▓   ▓       ▓▓▓▓▓     ▓  \n" \
         "▓    ▓  ▓       ▓       ▓        ▓ ▓ \n" \
         "▓    ▓  ▓▓▓     ▓       ▓▓▓     ▓   ▓\n" \
         "▓▓▓▓▓   ▓       ▓       ▓       ▓▓▓▓▓\n" \
         "▓       ▓▓▓▓▓   ▓▓▓▓▓   ▓▓▓▓▓   ▓   ▓"

DIE = "▓▓    ▓  ▓▓▓▓\n" \
      "▓ ▓   ▓  ▓   \n" \
      "▓ ▓   ▓  ▓▓▓ \n" \
      "▓ ▓   ▓  ▓   \n" \
      "▓▓    ▓  ▓▓▓"

GG = "▓▓▓▓   ▓▓▓▓\n" \
     "▓      ▓   \n" \
     "▓  ▓   ▓  ▓\n" \
     "▓▓▓▓   ▓▓▓▓\n"

while end_game == False:
    print(titulo)
    trainer = None
    while poke_explore == True:
        os.system("cls")
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")
            for coordinate_x in range(MAP_WIDTH):
                char_to_draw = " "
                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "O"
                for map_trainer in map_trainers:
                    if map_trainer[POS_X] == coordinate_x and map_trainer[POS_Y] == coordinate_y:
                        char_to_draw = "0"
                    if obstacles_definition[coordinate_y][coordinate_x] == "▓":
                        char_to_draw = "▓"
                        obstacle_in_cell = obstacles_definition[coordinate_y][coordinate_x]
                    if map_trainer[POS_X] == my_position[POS_X] and map_trainer[POS_Y] == my_position[POS_Y]:
                        poke_explore = False
                        poke_battle = True
                        trainer = [map_trainer[POS_X],map_trainer[POS_Y]]


                print(" {} ".format(char_to_draw), end="")
            print("|")
        print("+"+ "-" * MAP_WIDTH*3 + "+")
        direction = readchar.readchar().decode()
        if direction == "w" or direction == "W":
            my_position[POS_Y] -= 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction == "s" or direction == "S":
            my_position[POS_Y] += 1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction == "a" or direction == "A":
            my_position[POS_X] -= 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction == "d" or direction == "D":
            my_position[POS_X] += 1
            my_position[POS_X] %= MAP_WIDTH
        elif direction == "q" or direction == "Q":
            poke_explore = False
            end_game = True
    while poke_battle == True:
        vida_squirt = 80
        print("TE HAS ENCONTRADO CON UN ENTRENADOR POKEMON")
        while True:
            if trainer == map_trainers[0]:
                print(pelea)
                print("Turno de Pikachu")
                ataque_pika = randint(1, 2)
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
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_pika = int(vida_pika) * CANTIDAD_DE_BARRA / vida_total_pika
                barra_pika = ("[" + "⬛" * (int(valor_pika)) + "-" * (int(CANTIDAD_DE_BARRA - valor_pika)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Pikachu:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_pika, vida_pika, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
                os.system("cls")
            if trainer == map_trainers[1]:
                print(pelea)
                print("Turno de Bulbasur")
                ataque_bulba = randint(1, 2)
                if ataque_bulba == 1:
                    print("Ataque de Látigo Cepa")
                    vida_squirt -= 8
                else:
                    print("Ataque de Drenadoras")
                    vida_squirt -= 7

                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_bulbasour < 0:
                    vida_bulbasour = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_bulba = int(vida_bulbasour) * CANTIDAD_DE_BARRA / vida_total_bulbasour
                barra_bulba = ("[" + "⬛" * (int(valor_bulba)) + "-" * (int(CANTIDAD_DE_BARRA - valor_bulba)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Bulbasur:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_bulba, vida_bulbasour, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
                os.system("cls")

            if trainer == map_trainers[2]:
                print(pelea)
                print("Turno de Charmander")
                ataque_charman = randint(1, 2)
                if ataque_charman == 1:
                    print("Ataque de Furia Dragón")
                    vida_squirt -= 15
                else:
                    print("Ataque de Pantalla de Humo")
                    vida_squirt -= 8

                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_charman < 0:
                    vida_charman = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_charman = int(vida_charman) * CANTIDAD_DE_BARRA / vida_total_charman
                barra_charman = ("[" + "⬛" * (int(valor_charman)) + "-" * (int(CANTIDAD_DE_BARRA - valor_charman)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Charmander:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_charman, vida_charman, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
                os.system("cls")
            if trainer == map_trainers[3]:
                print(pelea)
                print("Turno de Mewtwo")
                ataque_mewtwo = randint(1, 2)
                if ataque_mewtwo == 1:
                    print("Ataque de Onda Certera")
                    vida_squirt -= 10
                else:
                    print("Curacion")
                    vida_mewtwo += 8

                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_mewtwo < 0:
                    vida_mewtwo = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_mewtwo = int(vida_mewtwo) * CANTIDAD_DE_BARRA / vida_total_mewtwo
                barra_mewtwo = ("[" + "⬛" * (int(valor_mewtwo)) + "-" * (int(CANTIDAD_DE_BARRA - valor_mewtwo)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Mewtwo:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_mewtwo, vida_mewtwo, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
                os.system("cls")
            if vida_squirt == 0:
                break
                died = True
            print(pelea)
            print("Turno de Squirtle")
            ataque_squirt = None
            while ataque_squirt not in ["P", "A", "B", "N","RORRO PIRRORO"]:
                ataque_squirt = input("¿Que ataque deseas hacer?\n"
                                      "P = Placaje\n"
                                      "A = Pistola de agua\n"
                                      "B = Burbuja\n"
                                      "N = Nada\n")

            if ataque_squirt == "P":
                print("Squirtle ataca con placaje")
                enemy_life = 10
                vida_squirt += 5
            elif ataque_squirt == "A":
                print("Squirtle ataca con Pistola de Agua")
                enemy_life = 12
            elif ataque_squirt == "B":
                print("Suirtle ataca con Burbuja")
                enemy_life = 15
            elif ataque_squirt == "N":
                print("Squirtle no hace nada")
            elif ataque_squirt == "RORRO PIRRORO":
                vida_squirt = 80
            if trainer == map_trainers[0]:
                vida_pika -= enemy_life
                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_pika < 0:
                    vida_pika = 0

                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_pika = int(vida_pika) * CANTIDAD_DE_BARRA / vida_total_pika
                barra_pika = ("[" + "⬛" * (int(valor_pika)) + "-" * (int(CANTIDAD_DE_BARRA - valor_pika)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Pikachu:   {} Vida: {}\n"
                      "Squirtle:   {} Vida: {}\n".format(barra_pika, vida_pika, barra_squirt, vida_squirt))

                input("Enter para continuar...\n\n")
                os.system("cls")
            if trainer == map_trainers[1]:
                vida_bulbasour -= enemy_life
                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_bulbasour < 0:
                    vida_bulbasour = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_bulba = int(vida_bulbasour) * CANTIDAD_DE_BARRA / vida_total_bulbasour
                barra_bulba = ("[" + "⬛" * (int(valor_bulba)) + "-" * (int(CANTIDAD_DE_BARRA - valor_bulba)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Pikachu:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_bulba, vida_bulbasour, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
            if trainer == map_trainers[2]:
                vida_charman -= enemy_life
                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_charman < 0:
                    vida_charman = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_charman = int(vida_charman) * CANTIDAD_DE_BARRA / vida_total_charman
                barra_charman = ("[" + "⬛" * (int(valor_charman)) + "-" * (int(CANTIDAD_DE_BARRA - valor_charman)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Charmander:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_charman, vida_charman, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
            if trainer == map_trainers[3]:
                vida_mewtwo -= enemy_life
                if vida_squirt < 0:
                    vida_squirt = 0
                if vida_mewtwo < 0:
                    vida_mewtwo = 0
                valor_squirt = int(vida_squirt) * CANTIDAD_DE_BARRA / vida_total_squirt
                valor_mewtwo = int(vida_mewtwo) * CANTIDAD_DE_BARRA / vida_total_mewtwo
                barra_mewtwo = ("[" + "⬛" * (int(valor_mewtwo)) + "-" * (int(CANTIDAD_DE_BARRA - valor_mewtwo)) + "]")
                barra_squirt = ("[" + "⬛" * (int(valor_squirt)) + "-" * (int(CANTIDAD_DE_BARRA - valor_squirt)) + "]")
                print("Mewtwo:   {} {}\n"
                      "Squirtle:   {} {}\n".format(barra_mewtwo, vida_mewtwo, barra_squirt, vida_squirt))
                input("Enter para continuar...\n\n")
            os.system("cls")
            if vida_pika == 0 and map_trainers[0] == trainer or vida_bulbasour == 0 and map_trainers[1] == trainer \
                    or vida_charman == 0 and map_trainers[2] == trainer or vida_mewtwo == 0 and map_trainers[3] == trainer:
                break
                exit = True
        if vida_squirt <= 0:
            if vida_pika < vida_total_pika:
                print("Squirtle Pierde el ganador Pikachu gana con {} de vida".format(vida_pika))
            elif vida_bulbasour < vida_total_bulbasour:
                print("Squirtle Pierde el ganador Bulbasur gana con {} de vida".format(vida_bulbasour))
            elif vida_charman < vida_total_charman:
                print("Squirtle Pierde el ganador Charmander gana con {} de vida".format(vida_charman))
            elif vida_mewtwo < vida_total_mewtwo:
                print("Squirtle Pierde el ganador Mewtwo gana con {} de vida".format(vida_mewtwo))
            end_game = True
        elif map_trainers[0] == trainer and vida_pika <= 0:
            print("Pikachu Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
            map_trainers[0] = [-1,-1]
        elif map_trainers[1] == trainer and vida_bulbasour <= 0:
            print("Bulbasur Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
            map_trainers[1] = [-1,-1]
        elif map_trainers[2] == trainer and vida_charman <= 0:
            print("Charmander Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
            map_trainers[2] = [-1,-1]
        elif map_trainers[3] == trainer and vida_mewtwo <= 0:
            print("Mewtwo Pierde, el ganador es Squirtle con {} de vida".format(vida_squirt))
            map_trainers[3] = [-1,-1]
        if map_trainer[0] == [-1,-1] and map_trainer[1] == [-1,-1] and \
                map_trainer[2] == [-1,-1] and map_trainer[3] == [-1,-1]:
                end_game = True

        input("Enter Para continuar...")

        poke_explore = True
        poke_battle = False

if died == True:
    print(DIE)
if exit == True:
    print(GG)


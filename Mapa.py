import os
import readchar
import random
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
map_objects = []
my_position = [3,1]
for i in range(10):
    x = random.randint(1,19)
    y = random.randint(1,14)
    object = [x,y]
    map_objects.append(object)

while True:
    print("+"+ "-" * MAP_WIDTH*3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                if map_object[POS_X] == my_position[POS_X] and map_object[POS_Y] == my_position[POS_Y]:
                    map_object[POS_X] = -1
                    map_object[POS_Y] = -1
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"


            print(" {} ".format(char_to_draw), end ="")
        print("|")
    print("+"+ "-" * MAP_WIDTH*3 + "+")

    #Ask user where he wants to move
    #direction = input("¿Dónde te quieres mover? [WASD]")
    direction = readchar.readchar().decode()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break
    os.system("cls")
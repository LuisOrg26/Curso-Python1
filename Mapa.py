import os
import readchar
import random
POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
map_objects = []
my_position = [3,1]
tall_lenght = 0
tail = []
for i in range(10):
    map_objects.append([random.randint(0,MAP_WIDTH),random.randint(0,MAP_HEIGHT)])

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
                    tall_lenght +=1
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"


            print(" {} ".format(char_to_draw), end ="")
        print("|")
    print("+"+ "-" * MAP_WIDTH*3 + "+")
    print("cola: {}".format(tail))

    #Ask user where he wants to move
    #direction = input("¿Dónde te quieres mover? [WASD]")
    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0,my_position.copy())
        tail = tail[:tall_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tall_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tall_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tall_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "q":
        break
    os.system("cls")
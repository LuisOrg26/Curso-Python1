import os
import readchar
import random
POS_X = 0
POS_Y = 1
NUMBER_OF_OBJECTS = 1
map_objects = []
my_position = [1,1]
tall_lenght = 0
tail = []
obstacle_definition = """▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓  ▓▓▓▓▓▓▓    ▓▓▓▓▓▓
▓                ▓▓▓
▓▓   ▓▓▓▓▓▓▓▓     ▓▓
▓▓   ▓▓▓▓▓▓      ▓▓▓
▓▓               ▓▓▓
▓▓▓▓  ▓▓▓   ▓▓▓  ▓▓▓
▓▓▓▓   ▓▓    ▓▓   ▓▓
▓▓▓     ▓    ▓▓     
▓▓             ▓▓   
▓▓     ▓▓▓▓    ▓▓   
▓▓    ▓▓▓▓▓▓▓   ▓▓  
▓               ▓▓  
      ▓▓▓▓▓▓    ▓▓  """
end_game = False
died = False
exit = False
obstacle_in_object = False
obstacles_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacles_definition[0])
MAP_HEIGHT = len(obstacles_definition)
for i in range(NUMBER_OF_OBJECTS):
    x = random.randint(0, MAP_WIDTH-1)
    y = random.randint(0, MAP_HEIGHT-1)
    while obstacles_definition[y][x]!= " ":
        x = random.randint(0, MAP_WIDTH)
        y = random.randint(0, MAP_HEIGHT)
    else:
        map_objects.append([x,y])


while not end_game ==True:
    os.system("cls")
    print("+"+ "-" * MAP_WIDTH*3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            tail_in_cell = None
            char_to_draw = " "
            obstacle_in_cell = None
            obstacle_in_object = False
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "+"
                    tail_in_cell = tail_piece
            if obstacles_definition[coordinate_y][coordinate_x] =="▓":
                char_to_draw = "▓"
                obstacle_in_cell = obstacles_definition[coordinate_y][coordinate_x]
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"
                if tail_in_cell:
                    end_game = True
                    died = True
                if obstacle_in_cell:
                    end_game = True
                    died = True
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                if map_object[POS_X] == my_position[POS_X] and map_object[POS_Y] == my_position[POS_Y]:
                    map_object[POS_X] = -1
                    map_object[POS_Y] = -1
                    tall_lenght +=1
                    x = random.randint(0, MAP_WIDTH-1)
                    y = random.randint(0, MAP_HEIGHT-1)
                    while obstacles_definition[y][x]!= " ":
                        x = random.randint(0, MAP_WIDTH-1)
                        y = random.randint(0, MAP_HEIGHT-1)
                    map_objects.append([x, y])


            print(" {} ".format(char_to_draw), end ="")
        print("|")
    print("+"+ "-" * MAP_WIDTH*3 + "+")
    print("cola: {}".format(tall_lenght))
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
        end_game = True
        exit = True
    os.system("cls")

DIE = "▓▓    ▓  ▓▓▓▓\n" \
      "▓ ▓   ▓  ▓   \n" \
      "▓ ▓   ▓  ▓▓▓ \n" \
      "▓ ▓   ▓  ▓   \n" \
      "▓▓    ▓  ▓▓▓"
GG = "▓▓▓▓   ▓▓▓▓\n" \
     "▓      ▓   \n" \
     "▓  ▓   ▓  ▓\n" \
     "▓▓▓▓   ▓▓▓▓\n"
os.system("cls")
if died == True:
    print(DIE)
if exit == True:
    print(GG)
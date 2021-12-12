import string

texto_del_usuario = input("Introduzca un texto:\n")
mayus = 0

for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        mayus += 1

print("Las mayusculas son: {}".format(mayus))
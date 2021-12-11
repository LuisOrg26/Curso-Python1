#Test para saber que tan mexicano eres
# (Idea sacada del test de que tan colombiano eres de Ivan Camargo)
print("Bienvenido al ¿Qué tan mexicano eres? Test")
print("Son 5 preguntas y contestaras con S o N")
Puntaje = 0
p1 = str(input("Primera pregunta \n¿Sabes todas las funciones de las palabras verga y pedo?"))
if p1 == "S":
    Puntaje += 1
p2 = str(input("Segunda pregunta \n¿Si son las 12 de la noche te comes unos tacos?"))
if p2 == "S":
    Puntaje += 1
p3 = str(input("Tercera Pregunta\nSi te encuentras con un bache con la forma de la virgen de Guadalupe, ¿Le haces un altar?"))
if p3 == "S":
    Puntaje += 1
p4 = str(input("Cuarta pregunta \n¿Odias las cobijas de tigres?"))
if p4 == "N":
    Puntaje += 1
p5 = str(input("Quinta pregunta \n¿Sabes quien es Roberto Gomez Bolaños?"))
if p4 == "S":
    Puntaje += 1
if Puntaje >= 2:
    print("Tu puntuacion fue de {}, No formas parte de la comunidad de mexichangos\n, "
          "asi que le lanzo un bolillo y regrese a su pais".format(Puntaje))
if 3<= Puntaje >= 4:
    print("Tu puntuacion fue de {}, Eres mexicano pero de esos que les da miedo ir en camion\n,"
          "no te preocupes eres bienvenido en Polanco y San Pedro".format(Puntaje))
if Puntaje == 5:
    print("Tu puntuacion fue de {}, ahuevo eres mexicano hasta los huesos\n,"
          "Te espero con gusto en Ecatepec para que termines como queso suizo".format(Puntaje))

#Si ven algo que pueda mejorar diganme paro





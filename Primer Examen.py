import random
numero1 = random.randint(1,100)
numero2 = random.randint(1,100)

palo = False
desodorante = False
Titulo = ("Bienvenido a Escapando de Jugadores de LoL")
print(Titulo,"\n"+"-"*len(Titulo),"\n")
print("Contexto: \nEstas en una convencion de League of Legends porque tu hermano queria ir\n"
      "Estas atrapado por las siguientes 3 horas\n"
      "Pero encuentras una escalera que te lleva a la ventilacion para poder escapar")
p1 = str(input("¿Subes la escalera o decides buscar otra salida?\n"
               "A = Subo las escaleras \n"
               "B = Busco otra salida \n"))
if p1 == "A":
    print("Subes las escaleras rapidamente y al estar en ventilacion"
          "te encuentras entre ir a la izquierda o a la derecha")
    p2 = str(input("A = Izquierda\n"
                   "B = Derecha\n"))
    if p2 == "A":
        print("Vas a la izquierda y te encuentras con un jugador de Teemo\n"
              "esta lleno de mugre y con una joroba de golum\n"
              "Puedes pelear con el o regresarte")
        p3 = str(input("A = Peleas\n"
                       "B = Huyes\n"))
        if p3 == "A":
            print("Decides pelear, pero no contabas con que el jugador de Teemo tenia una navaja\n"
                  "Te gana el main teemo y decide decirte - GG facil el tutorial\n")
            final1 = ("BAD ENDING: pierdes contra un jugador de teemo y la humillacion es tal que no te aceptan en el cielo")
            print(final1,"\n"+"-"*len(final1))
            exit()
        if p3 == "B":
            print("Empiezas a huir, pero el jugador de teemo ya registro tu olor y decide ir a por ti\n"
                  "No eres lo suficiente mente rapido para perderlo entonces te navajea por la espalda\n")
            final2 = (
                "WORST ENDING: Sobrevives pero tienes que vivir con la humillacion de escapar de un jugador de teemo")
            print(final2, "\n" + "-" * len(final2))
            exit()
    if p2 == "B":
        print("Te encuentras con un palo ¿Lo agarras?\n")
        p4 = str(input("A = agarrarlo\n"
                       "B = no agarrarlo\n"))
        if p4 == "A":
            palo = True
            print("Agarras el palo, pero como no hay salida te regresas hacia la izquierda")
            print("te encuentras con un jugador de Teemo\n"
                  "esta lleno de mugre y con una joroba de golum\n"
                  "Puedes pelear con el o regresarte")
            p5 = str(input("A = Peleas\n"
                           "B = Huyes\n"))
            if p5 == "A":
                print("Peleas contra el \n"
                      "El saca una navaja, pero tu tienes un palo\n"
                      "Le pegas con el palo y el se va corriendo en 4 patas\n")
                feliz = ("Felicidades haz vencido al desagradable main teemo")
                print(feliz, "\n" + "-" * len(feliz)+"\n")
                print("Despues de un rato sales de ventilacion\n"
                      "Te encuentras en la salida pero alguien te estorba\n"
                      "ES UN COSPLAYER DE YI\n"
                      "El te hace la siguiente pregunta")
                resultado = numero1 * numero2
                pregunta1 = int(input("Hola viajero para poder salir tienes que contestar la siguiente pregunta\n"
                                      "Cual es el daño de la Q de Yi a nivel 12 con guinso\n"
                                      "Te dare una ayuda el resultado es la multiplicaion de {} y {}\n"
                                      "Suerte Viajero\n".format(numero1,numero2)))
                if pregunta1 == resultado:
                    print("Felicidades haz contestado correctamente la pregunta\n"
                          "Te deja salir pero te da una nalgada\n")
                    final3 = ("NORMAL ENDING: Sales de la convencion pero con la dignidad en los suelos")
                    print(final3, "\n" + "-" * len(final3))
                    exit()
                if pregunta1 != resultado:
                    print("TU RESPUESTA ES INCORRECTA BASURA\n"
                          "El cosplayer te da una patada y te regresa a la convencion\n")
                    final4 =("DESTRUCTIVE ENDING: Acabas con 5 costillas rotas y te quedas en la convencion hasta que acabe")
                    print(final4, "\n" + "-" * len(final4))
                    exit()
        if p4 == "B":
            print("no agarras el palo pero como no hay salida te vas a la izquierda\n")
            print("te encuentras con un jugador de Teemo\n"
                  "esta lleno de mugre y con una joroba de golum\n"
                  "Puedes pelear con el o regresarte")
            p6 = str(input("A = Peleas\n"
                           "B = Huyes\n"))
            if p6 == "A":
                print("Decides pelear, pero no contabas con que el jugador de Teemo tenia una navaja\n"
                      "Te gana el main teemo y decide decirte - GG facil el tutorial\n")
                final1 = (
                    "BAD ENDING: pierdes contra un jugador de teemo y la humillacion es tal que no te aceptan en el cielo")
                print(final1, "\n" + "-" * len(final1))
                exit()
            if p6 == "B":
                print("Empiezas a huir, pero el jugador de teemo ya registro tu olor y decide ir a por ti\n"
                      "No eres lo suficiente mente rapido para perderlo entonces te navajea por la espalda\n")
                final2 = (
                    "WORST ENDING: Sobrevives pero tienes que vivir con la humillacion de escapar de un jugador de teemo")
                print(final2, "\n" + "-" * len(final2))
                exit()

if p1 == "B":
    print("Decides buscar otra salida\n"
          "En tu travesia te encuentras con desodorante en aerosol\n"
          "¿Lo agarras?\n")
    p7 = str(input("A = Si\n"
                   "B = No\n"))
    if p7 == "A":
        desodorante = True
        print("Buena decision en agarrar el desodorante\n"
              "Es muy probable que lo ocupemos en un futuro\n")
        feliz2 = ("Objeto adquirido: Desodorante en aerosol")
        print(feliz2, "\n" + "-" * len(feliz2)+"\n")
        print("Caminas un poco mas y entras a un show\n"
              "Es la final de LoL en Canada vista desde un proyector\n"
              "La gente tiene un cierto nivel de sobrepeso y el olor es comparable con menudo cociendose\n"
              "¿Quieres pasar o esperar a que se acabe el show?")
        p8 = str(input("A = Pasar\n"
                       "B = Esperar\n"))
        if p8 == "A":
            print("Decides pasar con 2 cubrebocas y desodorante en la mano\n"
                  "Empiezas a lanzarle desodorante y ellos gritan como si los estuvieran exorcizando\n")
            feliz3 = ("FELICIDADES HAZ PASADO DE LOS JUGADORES DE LOL")
            print(feliz3, "\n" + "-" * len(feliz3) + "\n")
            print("Despues de caminar unos 5 minutos te encuentras con la unica mujer de la convencion\n"
                  "Esta siendo acosada por un jugador vestido de Gragas\n"
                  "¿Peleas o Corres?\n")
            p9 = str(input("A = Pelear\n"
                           "B = Correr\n"))
            if p9 == "A":
                print("Peleas con Gragas\n"
                      "Al pelear con el le logras ganar\n"
                      "El ya debil te dice:\n"
                      "Lograste ganarme, pero si no adivinas el numero en el que estoy pensando traere a mis amigos\n"
                      "Te dare una pista es la resta de {} y {}".format(numero1,numero2))
                resultado2 = numero1-numero2
                p10 = int(input("¿Cual sera ese numero?\n"))
                if p10 == resultado2:
                    print("Felicidades haz derrotado a Gragas\n"
                          "La mujer te da las gracias y te acompaña a la salida\n")
                    final5 = ("ROMANTIC ENDING: Te casas y tienes dos hijos, los llamas Yasuo y Yone")
                    print(final5, "\n" + "-" * len(final5))
                    exit()
                if p10 != resultado2:
                    print("Oh no Gragas a llamado a sus amigos\n"
                          "llegan dos personas disfrazadas de Urgot y Alistar\n"
                          "Te rompen el hocico y te quedas solo\n")
                    final6 = ("SAD ENDING: Te llevan al hospital pero no pudiste proteger a la mujer")
                    print(final6, "\n" + "-" * len(final6))
                    exit()
            if p9 == "B":
                print("Corres pero Gragas te atrapa y te rompe un brazo\n")
                final7 = ("SAD ENDING: Te llevan al hospital pero no pudiste proteger a la mujer")
                print(final7, "\n" + "-" * len(final7))
                exit()
        if p8 == "B":
            print("Esperas 5 horas, pero el olor hizo que te desmayaras\n")
            final8 = ("DISGUSTING ENDING: te ahogas con el olor y te tienes que desintoxicar por 1 mes")
            print(final8, "\n" + "-" * len(final8))
            exit()
    if p7 == "B":
        print("No agarras el desodorante\n"
              "Caminas un poco mas y te encuentras con un show de LoL\n"
              "Es la final el torneo mundial en Canada vista desde un proyector\n"
              "No puedes salir y el olor es comparable con el de menudo cociendose\n")
        final9 = ("DISGUSTING ENDING: te ahogas con el olor y te tienes que desintoxicar por 1 mes")
        print(final9, "\n" + "-" * len(final9))
        exit()

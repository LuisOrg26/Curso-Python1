import random
num = random.randint(1,10)
num2 = int(input("Elije un numero del 1 al 10: "))
if num == num2:
    print("felicidades elegiste esl numero correcto")
else:
    print("tu numero no es igual")

print("el numero correcto era: {}".format(num))
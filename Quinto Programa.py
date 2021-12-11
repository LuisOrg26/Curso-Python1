
edad = int(input("¿Cual es tu edad? "))
carnet = input("Digame su tipo de carnet \nE para estudiante\nP para Pensionista\nF de Familia numerosa\nN para nada\n")
if (edad < 35 and edad > 25 and carnet =="E") or edad < 10 or (edad > 65 and carnet == "P") or (carnet =="F"):
    print("Se te aplica el descuento")
else:
    print("No hay descuento")
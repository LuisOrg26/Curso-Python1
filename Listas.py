#Texto de Prueba
Compras = []
articulo = ""
siguiente = ""
Titulo = "Lista de la Compra"
print("{}\n".format(Titulo)+"-"*len(Titulo))

while articulo != "Q":
    siguiente = ""
    articulo = str(input("¿Que desea Comprar?\n"
                         "(Presione Q para salir)\n"))
    if articulo == "Q":
        break
    while siguiente not in ["S","N"]:
        siguiente = str(input("¿Seguro que quiere agregar {}?\nPresione (S/N)\n".format(articulo)))

    if siguiente == "S":
        print("{} agregado".format(articulo))
        Compras.append(articulo)
    elif siguiente == "N":
        print("{} no agregado".format(articulo))

print("La lista de compras es:\n")
for i in range(len(Compras)):
    print(Compras[i])



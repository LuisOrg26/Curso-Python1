from random import randint

def check(list):
    art = input("¿Cual es el producto que quiere añadir a la lista?")
    if art in list:
        print("Este producto ya existe")
        continu = str(input("¿Quiere añadir otro producto? (S/N)\n"))
        if continu == "S":
            check(list)
        else:
            pass
    else:
        lista_de_compra.append(art)
        print("se ha añadido exitosamente el producto")



if __name__ == "__main__":
    lista_de_compra = ["huevo","pollo","frijol"]
    check(lista_de_compra)
    print(lista_de_compra)
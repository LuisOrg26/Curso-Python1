
def main(jitomates):
    precio_del_jitomate = jitomates * 50
    return precio_del_jitomate


if __name__ == "__main__":
    cantidad =int(input("¿Cuantos jitomates tienes?"))
    jito = main(cantidad)
    print("El jitomate te va a costar ${} pesos".format(jito))
def par_o_impar(number):
    par = number % 2
    if par == 1:
        impar = True
    if par == 0:
        impar = False
    return impar

if __name__ == "__main__":
    print("El numero es impar: {}".format(par_o_impar(4)))
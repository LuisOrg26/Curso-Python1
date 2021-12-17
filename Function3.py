def string_mas_larga(string,*args):
    mayor = []
    mayor.append(string)
    if args:
        for i in args:
            mayor.append(i)
    maximo = max(mayor,key=len)
    return maximo

if __name__ == "__main__":
    print(string_mas_larga("hola","soy","zorman"))
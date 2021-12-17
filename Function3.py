def suma(list):
    nuevo = 0
    for i in list:
        nuevo += i
    return nuevo

if __name__ == "__main__":
    print(suma([1,5,6,7,8]))
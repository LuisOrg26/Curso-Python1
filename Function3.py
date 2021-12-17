def safe(seguro):
    if seguro == "S":
        secure = True
    if seguro == "N":
        secure = False
    return secure

if __name__ == "__main__":
    secure = str(input("¿Estas seguro? (S/N)\n"))
    print(safe(secure))
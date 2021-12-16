def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)




if __name__ == "__main__":
    for a in range(10):
        print(fibonacci(a))




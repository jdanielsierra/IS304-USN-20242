numeros = list(range(1, 101))


i = 0


while i < len(numeros):
    if numeros[i] % 3 == 0 and numeros[i] % 5 == 0:
        numeros[i] = "fizzbuzz"
    elif numeros[i] % 3 == 0:
        numeros[i] = "fizz"
    elif numeros[i] % 5 == 0:
        numeros[i] = "buzz"
    i += 1


print(numeros)

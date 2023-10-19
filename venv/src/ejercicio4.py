def cuantatras(numero):
    listanum = []
    for num in range(numero+1):
        listanum.append(num)
    listanum.reverse()
    return listanum


if __name__ == "__main__":
    numero = int(input("Ponga un numero: "))
    numeros = cuantatras(numero)
    for x in numeros:
        print(x, end=", ")

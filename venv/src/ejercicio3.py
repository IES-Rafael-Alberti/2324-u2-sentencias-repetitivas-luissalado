

def comprobarpar(numero):
    listanum = []
    for num in range(1,numero):
        if num % 2 == 0:
            pass
        else:
            listanum.append(num)
    return listanum



if __name__ == "__main__":
    numero = int(input("Escribe un numero entero: "))
    print(comprobarpar(numero))

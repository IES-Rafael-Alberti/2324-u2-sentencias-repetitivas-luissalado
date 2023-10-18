##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces



def mostrar(palabra):
    cont = 0
    while cont < 9:
        cont = cont +1
        print(palabra)
    return palabra

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    print(mostrar(palabra))
##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.

##proceso


def comprobarpar(numero):
    listanum = []
    for num in range(1,numero):
        if num % 2 == 0:
            pass
        else:
            listanum.append(num)
    return listanum

def mensaje():
    print(comprobarpar(numero))


if __name__ == "__main__":
    
    ##entrada
    numero = int(input("Escribe un numero entero: "))
    
    ##salida
    
    mensaje()


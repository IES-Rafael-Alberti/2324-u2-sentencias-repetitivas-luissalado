##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
# desde ese número hasta cero separados por comas.


##proceso

def cuantatras(numero):
    listanum = []
    for num in range(numero+1):
        listanum.append(num)
    listanum.reverse()
    return listanum

def mensaje():
    numeros = cuantatras(numero)
    for x in numeros:
        print(x, end=", ")
if __name__ == "__main__":
    
    ##entrada
    numero = int(input("Ponga un numero: "))
    
    ##salida
    mensaje()


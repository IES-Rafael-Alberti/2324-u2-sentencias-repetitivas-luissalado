## Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no.

##PROCESO

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def comprobar(numero):
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
        
        
if __name__ == "__main__":
    
    ##ENTRADA
    
    numero = int(input("Escribe un numero: "))
    
    ## SALIDA
    
    comprobar(numero)
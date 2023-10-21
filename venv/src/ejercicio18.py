## Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


##proceso


def par(n):
    pares = 0
    while n != -1:
        if n % 2 == 0:
            pares += 1
        suma = 0
        vtemporal = n
        while vtemporal != 0:
            digito = vtemporal % 10
            suma += digito
            vtemporal = vtemporal // 10
        print("Suma de sus digitos:", suma)
        n = int(input("Nmero (-1 para terminar el programa): "))
    return pares

def mensaje():
    resultado = par(n)
    print("Se ingresaron", resultado, "pares")

if __name__ == "__main__":
    
    ##entrada
    
    n = int(input("Nmero (-1 para terminar el programa): "))
    
    ## Salida

    mensaje()
## Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

##PROCESO


def sumadigitos(num):
    suma = 0
    while num != 0:
        digito = num % 10
        suma += digito
        num = num // 10
    return suma

def mensaje():
    resultado = sumadigitos(num)
    print("Suma de los digitos:", resultado)
    
if __name__ == "__main__":
    
    ##ENTRADA
    
    num = int(input("Escriba un numero: "))
    
    ##SALIDA
    
    mensaje()
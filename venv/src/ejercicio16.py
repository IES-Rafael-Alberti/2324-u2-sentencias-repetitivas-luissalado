## Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

##PROCESO

def mayor(num):
    mayor = -1
    while num > 0:
        if num > mayor:
            mayor = num
        num = int(input("Número positivo: "))
    return mayor


def mensaje():
    resultado = mayor(num)
    print("Mayor número ingresado:", resultado)
   
    
if __name__ == "__main__":
    
    ##ENTRADA
    num = int(input("Número positivo: "))
    
    ##SALIDA
    mensaje()
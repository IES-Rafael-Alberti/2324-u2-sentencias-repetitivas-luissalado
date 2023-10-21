## Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


##proceso

def solicitar(n):
    cantidad = 0
    while n != 0:
        primo = True
        for i in range(2, n):
            if n % i == 0:
                primo = False
                break
        if primo:
            cantidad += 1
        n = int(input("Número: "))
    return cantidad

def mensaje():
    resultado = solicitar(n)
    print("Primos:", resultado)
    
    
if __name__ == "__main__":
    
    ##ENTRADA
    n = int(input("Número: "))
     
     
    ##SALIDA
     
    mensaje()














## Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

##PROCESO


def numero(num):
    resultado = ""
    for i in range(1, num + 1, 2):
        for j in range(i, 0, -2):
            resultado += str(j) + " "
        resultado += "\n"
    return resultado

if __name__ =="__main__":
    
    ##ENTRADA
    
    num = int(input("Dame un numero: "))
    
    ##SALIDA
    
    print(numero(num))
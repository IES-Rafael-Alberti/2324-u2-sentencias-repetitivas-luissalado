##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
##rectángulo como el de más abajo, de altura el número introducido.


##PROCESO

def triangulo(altura):
    for i in range(1,altura):
        triangulo = i*"*"
    return triangulo


if __name__ == "__main__":


    ##ENTRADA

    altura = int(input("Cuanta altura quieres para el triangulo: "))


    ##SALIDA

    print(triangulo(altura))
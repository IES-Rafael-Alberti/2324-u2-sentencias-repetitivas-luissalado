##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
##rectángulo como el de más abajo, de altura el número introducido.


##PROCESO

def triangulo(altura):
    resultado = ""
    for i in range(altura):
        resultado += "*" * (i + 1) + "\n"
    return resultado


if __name__ == "__main__":


    ##ENTRADA

    altura = int(input("Cuanta altura quieres para el triangulo: "))


    ##SALIDA

    print(triangulo(altura))
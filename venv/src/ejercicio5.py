## Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
## capital obtenido en la inversión cada año que dura la inversión.



##PROCESO
def inversion(cantidad,interes,anos):
    anios_cantidad = []
    for num in range (anos):
        cantidad *= 1 + interes / 100
        anios_cantidad.append(cantidad)
    return anios_cantidad


if __name__ == "__main__":
    ##ENTRADA

    cantidad = float(input("Cuanta cantidad quieres invertir: "))
    interes = float(input("Interes porcentual anual: "))
    anos = int(input("Cuantos años quieres invertir: "))


    ##SALIDA   
    
    inversion_total = inversion(cantidad,interes,anos)
    for x in range(1, len(inversion_total)+1): ## el mas 1 es para que no imprima el numero 0
        print("El", x,"has obtenido", inversion_total[x-1]) ## l menos 1  esta porque se sale de rango

    print(inversion_total)
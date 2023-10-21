## Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


##PROCESO

def tabla(): 
    resultado = ""
    for i in range(1, 11):
        for j in range(1, 11):
            resultado += str(i * j) + "\t"
        resultado += "\n"
    return resultado
        
if __name__ == "__main__":
    
    ##SALIDA
    
    print(tabla())
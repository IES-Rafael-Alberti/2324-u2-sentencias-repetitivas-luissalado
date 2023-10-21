## Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

##PROCESO


def positivos():
    positivos = 0
    num = int(input("Número (0 para terminar): "))
    while num != 0:
        if num > 0:
            positivos += 1
        num = int(input("Número (0 para terminar): "))
    return positivos

def mensaje():
    resultado = positivos()
    print("Cantidad de positivos:", resultado) 
    

if __name__ == "__main__":
    
    ##ENTRADA
    
    num= int(input("Número (0 para terminar): "))
    
    ##salida
    
    mensaje()
 
 
    
  
    
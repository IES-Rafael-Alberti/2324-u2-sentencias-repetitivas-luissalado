##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces



def mostrar(palabra):
    for i in range(10):
        print(palabra)
    return palabra

def mensaje():
    resultado = mostrar(palabra)
    print(resultado)
    
    
if __name__ == "__main__":
    
    ##ENTRADA
    
    palabra = input("Escribe una palabra: ")
    
    ##SALIDA
    
    mensaje()

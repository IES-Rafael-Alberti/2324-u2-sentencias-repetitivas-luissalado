##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.




##PROCESO


def contar(palabra):
    alreves = ""
    for i in range(len(palabra)-1, -1, -1):
        alreves += palabra[i] + "\n"
    return alreves

if __name__ == "__main__":
    
    ##ENTRADA
    
    palabra = input("Escriba una palabra: ")

    
    ##SALIDA
    
    alreves = contar(palabra)
    print(alreves)
    
    
        
        
##Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

##PROCESO

def salida(frase):
    resultado = ""
    frase = None
    while frase != "salir":     
        frase = input("Escribe una frase: ")    
        if frase != "salir":
            resultado += frase + "\n"
    return resultado


if __name__ == "__main__":
    
    ##ENTRADA
    
    frase = input("Escribe una frase: ")
    
    ##Salida
    
    salida(frase)
    
    
    
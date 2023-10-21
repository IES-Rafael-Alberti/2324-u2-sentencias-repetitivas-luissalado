## Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
# Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, 
# indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
# Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución


##PROCESO

def analizar(frase, letra):
    i = 0
    while i != len(frase):
        if letra != frase[i]:
            print("No se encontró en la posición", i)
            i += 1
            continue
        else:
            print("Se encontró en la posición", i)
            return i
    return -1

def mensaje():
    resultado = analizar(frase, letra)
    if resultado == -1:
        print(f"La letra '{letra}' no fue encontrada en la frase.")
    else:
        print(f"La letra '{letra}' fue encontrada en la posición {resultado}.")

if __name__ =="__main__":
    
    ##ENTRADA
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra: ")
    
    ##SALIDA
    
    mensaje()


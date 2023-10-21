## Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


##PROCESO

def analiza(frase, letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    return contador


def mensaje():
    resultado = analiza(frase, letra)
    print(f"{letra} aparece {resultado} veces")
    
if __name__ == "__main__":
    
    ##ENTRAD
    
    
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    
    ##SALIDA
    
    mensaje()
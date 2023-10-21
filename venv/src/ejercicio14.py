## Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


##PROCESO


def sumatoria(numero):
    total = 0
    while numero != 0:
        total += numero
        numero = int(input("Número: "))
    return total

def mensaje():
    resultado = sumatoria(numero)
    print(f"La sumatoria es: {resultado}")

if __name__ == "__main__":
    
    
    
    # ENTRADA
    numero = int(input("Número: "))
    
    
    # Salida
    
    mensaje()
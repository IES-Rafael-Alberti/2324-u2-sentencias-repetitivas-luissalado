##Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
# ha cumplido (desde 1 hasta su edad).

##proceso

def anos(edad):
    result = []
    for num in range(edad):
        result.append(f"Tienes {num+1} años")
    return result

def mensaje():
    resultado = anos(edad)
    for r in resultado:
        print(r)
    

if __name__ == "__main__":
    
    ##ENTRADA
    edad = int(input("Ingresa tu edad: "))
    
    ##SALIDA
    
    mensaje()


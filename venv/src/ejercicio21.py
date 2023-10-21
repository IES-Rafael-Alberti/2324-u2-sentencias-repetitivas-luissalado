## Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
# no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, 
# informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

##PROCESO
def calcular_total_venta(monto):
    total = 0
    while monto != 0:
        if monto < 0:
            print("no valido")
        else:
            total += monto
        monto = float(input("Monto de una venta: "))
    if total > 1000:
        total -= total * 0.1
    return total

def mensaje():
    resultado = calcular_total_venta(monto)
    print("Monto a pagar: ", resultado)
    
if __name__ =="__main__":
    
    ##ENTRADA
    
    monto = float(input("Monto de una venta: ")) 
    
    ##salida
    
    mensaje()
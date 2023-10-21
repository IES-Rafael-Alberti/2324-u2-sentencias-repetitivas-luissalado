## Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

##PROCESO


def contraseña(input_usuario):
    contrasena = "contraseña"
    while True:
        input_usuario = input("Introduce la contraseña: ")
        if input_usuario == contrasena:
            return "Contraseña correcta. Acceso permitido."
        else:
            return "Contraseña incorrecta. Inténtalo de nuevo."
        
if __name__ == "__main__":
    
    ##ENTRADA
    
    input_usuario = input("Introduce la contraseña: ")
    
    
    ##SALIDA
    
    print(contraseña(input_usuario))
    
    
    
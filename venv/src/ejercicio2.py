def anos(edad):
    for num in range(edad):
        print("Tienes", num+1, "años")

if __name__ == "__main__":
    edad = int(input("Cuantos años tienes? "))
    anos(edad)

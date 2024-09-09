def sumarTerminos(a, b, c):
    suma = a + b + c
    return suma

def main():
    a = float(input("Ingrese el primer termino: "))
    b = float(input("Ingrese el segundo termino: "))
    c = float(input("Ingrese el tercer termino: "))
    resultado = sumarTerminos(a, b, c)
    print("El resultado es:", resultado)

main()

def calcularAreaRectangulo(altura, base):
    area = altura * base
    return area

def calcularAreaTriangulo(altura, base):
    area = (altura * base) * 0.5
    return area

# Función principal
def main():
    operacion = float(input("Que area desea calcular. Rectangulo [1] o Triangulo [2]: "))

    valorBase = float(input("Ingrese la base deseada: "))
    valorAltura = float(input("Ingrese la altura deseada "))

    if (operacion == 1):
        resultado = calcularAreaRectangulo(valorAltura, valorBase)
    elif (operacion == 2):
        resultado = calcularAreaTriangulo(valorAltura, valorBase)

    print (f"El valor del area es: {resultado}")

main()

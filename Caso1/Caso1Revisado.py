def multiplicacion(factor1, factor2):
    producto = factor1 * factor2
    return producto


if __name__=="__main__":
    multiplicando = float(input("Ingrese el multiplicando: "))
    multiplicador = float(input("Ingrese el multiplicador: "))

    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador}, el resultado es {resultado}")
#prueba
def main():
    a = int(input("Ingrese primer número: ", ))
    b = int(input("Ingrese segundo número: ", ))

    print("suma: ",suma(a,b))
    print("resta: ",resta(a,b))
    print("multiplicación: ",multiplicacion(a,b))
    print("división: ",division(a,b))
    # probando el programa


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

if __name__ == "__main__":
    main()
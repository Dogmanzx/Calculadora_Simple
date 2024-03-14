def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b
def potencia(a, b):
    return a ** b
import math
def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de número negativo"
    else:
        return math.sqrt(a)

    
while True:
    print("\nCalculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 7:
        break
    elif opcion == 6:
        num1 = float(input("Ingresa el número: "))
        print("Resultado: ", raiz_cuadrada(num1))
        continue

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print("Resultado: ", suma(num1, num2))
    elif opcion == 2:
        print("Resultado: ", resta(num1, num2))
    elif opcion == 3:
        print("Resultado: ", multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado: ", division(num1, num2))
    elif opcion == 5:
        print("Resultado: ", potencia(num1, num2))
    else:
        print("Opción inválida. Por favor, elige una opción entre 1 y 5.")
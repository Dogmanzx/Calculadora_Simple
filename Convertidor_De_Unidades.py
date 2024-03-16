Factor_De_Conversion = 2.2046

def kilos_a_libras(kilos):
    return kilos * Factor_De_Conversion

def libras_a_kilos(libras):
    return libras / Factor_De_Conversion

while True:
    print("\nConvertidor de Unidades")
    print("1. Kilos a Libras")
    print("2. Libras a Kilos")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 3:
        break

    num = float(input("Ingresa el número: "))

    if opcion == 1:
        print("Resultado: ", kilos_a_libras(num))
    elif opcion == 2:
        print("Resultado: ", libras_a_kilos(num))
    else:
        print("Opción inválida. Por favor, elige una opción entre 1 y 3.")
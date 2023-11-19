# Solicitar al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("\nMenú de opciones:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (primer número menos segundo número)")
print("3. Mostrar la multiplicación de los dos números")
#opciones
opcion = input("Elija una opción (1, 2 o 3): ")

if opcion == "1":
    resultado = numero1 + numero2
    print("La suma de {} y {} es: {}".format(numero1, numero2, resultado))
elif opcion == "2":
    resultado = numero1 - numero2
    print("La resta de {} y {} es: {}".format(numero1, numero2, resultado))
elif opcion == "3":
    resultado = numero1 * numero2
    print("La multiplicación de {} y {} es: {}".format(numero1, numero2, resultado))
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")

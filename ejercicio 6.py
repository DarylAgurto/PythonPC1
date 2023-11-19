# Solicitar al usuario la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0  
elif 4 <= edad <= 18:
    precio_entrada = 5  # Clientes de 4 a 18 años pagan 5
else:
    precio_entrada = 10  # Clientes < de 18 años pagan 10

print("El precio de la entrada es:{}".format(precio_entrada))

costo_comida = float(input(" costo de su comida:"))

propina = float(input("Ingrese el porcentaje de propina que dara: "))

propina = (propina / 100) * costo_comida

# dinero a dejar como propina
print("Debe dejar ${:.2f} como propina.".format(propina))


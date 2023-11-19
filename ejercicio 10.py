lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#en la siguiente parte del codigo me apoye con gpt un poco
posiciones_a_eliminar = [0, 4, 5]
for posicion in sorted(posiciones_a_eliminar, reverse=True):
    lista_muestra.pop(posicion)
#resultado 
print("Resultado esperado:", lista_muestra)

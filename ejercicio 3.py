
payasos = int(input(" payasos vendidos: "))
muñecas = int(input(" muñecas vendidas: "))

peso_payaso = 112  
peso_muñeca = 75   

peso_total_paquete = (payasos * peso_payaso) + (muñecas * peso_muñeca)

print("El peso total del paquete es de {} gramos.".format(peso_total_paquete))

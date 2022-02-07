"""
entradas
sueldo--->float--->sueldo
salidas
sueldofinal--->float--->salariofin
"""
sueldo=float(input("digite el sueldo del trabador: "))
if(sueldo<900000):
 salariofin=sueldo+(sueldo*0.15)
 print("el salario es de: "+str(salariofin))

else:
 salariofin=sueldo+(sueldo*0.12)
 print("el salario es: "+str(salariofin))
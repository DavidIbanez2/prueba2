"""
entradas
dato1--->int--->P
dato2--->int--->Q
salidas 
expresion--->int--->epre
"""
P=int(input("dale un valor a P: "))
Q=int(input("dale un valor a Q: "))
epre=((P)**3)+((Q)**5)-2*((P)**2)
 
if(epre<=680):
 print("P y Q satisface la exprexcion: "+str(epre)) 
 
else:
 print("P y Q no satisfacen la ecuacion: "+str(epre))
"""
entradas
A--->int--->A
B--->int--->B
C--->int--->C
D--->int--->D
salidas
ecuacion1--->float--->ecu1
ecuacion2--->float--->ecu2
"""
A=int(input("ingrese el valor de A: "))
B=int(input("ingrese el valor de B: "))
C=int(input("ingrese el valor de C: "))
D=int(input("ingrese el valor de D: "))
ecu1=(A-C)**2
if(D<=0):
 print("el resultado es: "+str(ecu1))
else:
 ecu2=(A-B)**3/D
 print("el resultado es: "+str(ecu2))
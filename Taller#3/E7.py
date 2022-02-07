"""
Entradas
kilimetrosrecorridos--->float--->km
Salidas
dinero a pagar--->float--->dn
"""
km=float(input("cuantos kilometros recorrio?: "))
if(km<=300 and km>0):
    dn=50000
    print("el total a pagar por el alquiler del vehiculo es: "+str(dn))

elif(km>=300 and km<=1000):
 dn=(70000+(km-300)*30000)
 print("el valor a pagar es: "+str(dn))

if(km>1000):
 dn=(150000+(km-300)*9000)
 print("el valor a pagar es: "+str(dn))

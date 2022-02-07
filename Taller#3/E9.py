"""
Entradas
nombre--->str--->nom
precio--->float--->din
salidas
descuento--->float--->des
totalapagar--->float--->total
"""
nom=str(input("Nombre del cliente: "))
din=float(input("Cuanto gasto: "))
if(din<=50000):
    print("no hay despuento")
elif(din>50000 and din>=100000):
 des=(din-(din*0.05))
 total=(din-des)
 print("el nombre del cliente es: "+str(nom)+(" el ciente compro: "+str(din))+(" el descuento es de: "+str(des))+(" el total a pagar es de: "+str(total)))
elif(din>100000 and din>=700000):
 des=(din-(din*0.11))
 total=(din-des)
 print("el nombre del cliente es: "+str(nom)+(" el ciente compro: "+str(din))+(" el descuento es de: "+str(des))+(" el total a pagar es de: "+str(total)))
elif(din>700000 and din>=1500000):
 des=(din-(din*0.18))
 total=(din-des)
 print("el nombre del cliente es: "+str(nom)+(" el ciente compro: "+str(din))+(" el descuento es de: "+str(des))+(" el total a pagar es de: "+str(total)))
elif(din>1500000):
 des=(din-(din*0.25))
 total=(din-des)
 print("el nombre del cliente es: "+str(nom)+(" el ciente compro: "+str(din))+(" el descuento es de: "+str(des))+(" el total a pagar es de: "+str(total)))
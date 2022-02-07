"""
Entradas
categoria--->int--->cat
salario--->int--->sal
salidas
aumento--->float--->aum
salariofinal--->float--->total
"""
cat=int(input("que categoria es: "))
if(cat==1):
 sal=5000000
 aum=(sal*0.10)
 total=sal+aum
 print("su salario bruto es: "+str(sal))+(" su aumento es de: "+str(aum))+(" su salario total es: "+str(total))
 
elif(cat==2):
 sal=4300000 
 aum=(sal*0.15)
 total=(sal+aum)    
 print("su salario bruto es: "+str(sal))+(" su aumento es de: "+str(aum))+(" su salario total es: "+str(total))

elif(cat==3):
 sal=3600000 
 aum=(sal*0.20)
 total=(sal+aum)
 print("su salario bruto es: "+str(sal))+(" su aumento es de: "+str(aum))+(" su salario total es: "+str(total))

elif(cat==4):
 sal=2000000 
 aum=(sal*0.40)
 total=(sal+aum)
 print("su salario bruto es: "+str(sal))+(" su aumento es de: "+str(aum))+(" su salario total es: "+str(total))

elif(cat==5):
 sal=900000 
 aum=(sal*0.60)
 total=(sal+aum)
 print("su salario bruto es: "+str(sal))+(" su aumento es de: "+str(aum))+(" su salario total es: "+str(total))
#EJERCICIO 7.- Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.

a = int(input("ingrese un numero :"))
b = int(input("ingrese otro numero : " ))

if a+b>0:
    print("positiva")
elif a+b<0:
    print("negativa")
else:
    print("es 0")	


#EJERCICIO 15.- Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.

adivinar=int(input("ingreseel numero secreto:"))
numero=int(input("otro numero:"))
numero=int(input("numero:"))

while numero!=adivinar:
    if numero>adivinar:
        print ("es menor")
    else:
        print ("es mayor")
    numero=int(input("numero:"))
print ("acertado")
"""1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

    Mostrar una suma de los dos números
    Mostrar una resta de los dos números (el primero menos el segundo)
    Mostrar una multiplicación de los dos números
    En caso de no introducir una opción válida, el programa informará de que no es correcta."""
    
s1 = int(input("ingrese un numero  "))
s2 = int(input("ingrese el otro numero "))
elegir = 0

print("¿que vas hacer primero? \n1) suma\n2) resta\n3) Multiplicar")

elegir = int(input("elija el número: ") ) 

if elegir == 1:
    print("La suma ",s1,"+",s2,"es",s1+s2)
elif elegir == 2:
    print("La resta ",s1,"-",s2,"es",s1-s2)
elif elegir == 3:
    print("El producto ",s1,"*",s2,"es",s1*s2)
else:
    print("incorrecta")
    

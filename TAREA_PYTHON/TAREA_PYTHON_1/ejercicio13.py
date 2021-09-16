#EJERCICIO 13.- Pedir un número por teclado y mostrar la tabla de multiplicar

multi = int(input("ingrese un numero para la tabla de multiplicacion"))
m = 1

while m <= 12:
    print(multi,"x", m, "=", multi*m)
    m+=1
print("aqui esta la tabla de multiplicar",multi)
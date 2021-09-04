# Python
#Sentencia If (true) : bool()

if True:
    print("Se cumple la condicion")
    print("A")
    variable_1 = 12
    
#Varios If simples
a = 2
b = 50

if a==2:
    print("Es par")
    
if b==2:
    print("Es par")


# Ifs Anidados   
if b!=5:
    print("No es multiplo es 5")
    if a>2:
        print("Es par")
        if b>=2:
            print("Es par")
            if a>=2:
                print("Es par")

#If else
if b==5:
    print("Es par")
else:
    print("Es impar")
#Sentencia elif
comando = "SALUDAR"

if comando == "ENTRAR":
    print("Bienvebido al sistema")
elif comando == "Saludar":
    print("Hola Mundo")
elif comando == "SALIR":
    print("saliendo del Sistema")
else:
    print("El comando no se reconoce")

print("Salir.....")
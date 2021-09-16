#EJERCICIO 10.- Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.

usuario = input("ingrese un usuario: ")
contraseña = input("ingrese la clave: ")

if usuario == "pepe" or contraseña == "passwd#":
    print("Has entrado al sistema")
else:
    print("error el inicio seccion")
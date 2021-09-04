# Lista en python

lista_enteros = [1,2,3,4,5]         # Lista de Enteros

lista_float = [1.0,2.0,3.5,4.5,5.5] # Lista de floats

lista_cadenas = ["A","B",'C','SE',"HO"] # Lista de string

lista_general = [1, 3.5, "Cadena1", True]  #Lista de tipo multiples
#                0   1      2        3
# Acceder a los elementos dde la lista: Se lo realiza mediante los indices : Posicion 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, n

print(lista_enteros[0],lista_enteros[-1])
print(lista_enteros[1],lista_enteros[-2])
print(lista_enteros[2])

# Slicing de lista en python

# Lista principal : lista_enteros
sub_lista_1 =  lista_general[0:2]
sub_lista_2 =  lista_general[2:]

print(sub_lista_2)
print(type(sub_lista_1))

print(sub_lista_2)
print(type(sub_lista_2))

print("--------")
print(type(lista_general))

# Operaciones con listas
#Suma   "+"

impares = [1,3,5,7,9]
pares = [2,4,6,8,10]

lista_total = impares + pares
print(lista_total)
print(type(lista_total))

#Modificar los elementos de la lista
#[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# 0  1  2  

lista_total[1] = 2
lista_total[2] = 3
lista_total[3] = 4
lista_total[4] = 5

print("Mi nueva lista es : \n")
print(lista_total)

#Agregar Elementos a un lista

lista_general = [1, 3.5, "Cadena1", True, [1,2,3,4] ]
print(f"Lista Original es : {lista_general}")

lista_general.append("Darwin")
print(f"Lista Modificada es : {lista_general}")

lista_general.append("Calle")
print(f"Lista Modificada es : {lista_general}")

lista_general.append(8+15)
print(f"Lista Modificada es : {lista_general}")

lista_general.append( (8+15)* 2 + (10/2) )
print(f"Lista Modificada es : {lista_general}")

lista_nueva = [True, False]

lista_general.append( lista_nueva )
print(f"Lista Modificada es : {lista_general}")

print(len(lista_general))
print(lista_general[len(lista_general)-1])

#Vacear un lista: Borrar todos los elementos de la lista

print(f"Lista Original: \n {lista_general}")

lista_general =[]
print("Lista Vacia ", lista_general)

# Definir una cadena : "Hola mundo Python"

frase_1 = "Hola Mundo Pyhton"

# Conversion de String a lista------->  funcion list()
l = list(frase_1)

print(type(1))
print(1)


#Lista Anidadas
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = [7,8,9]
lista_d = ['a','b','c']

#Lista anidadas
resultado = [lista_a, lista_b, lista_c, lista_d]

print("Lista Anidadas")
print(resultado)

print(resultado[0][-1])
print(resultado[1][2:])
print(resultado[2][:-1])
print(resultado[3][2:])













#Tuplas son Inmutables : No se pueden cambiar los datos que contiene dicha estructura

tupla_1 = (1,2,3,4,5,6,7,8,9,10) #tuplas de entero

tupla_2 = (True, False)  # tuplas de boolean

tupla_3 = (5.2, 7.4)    # tupla de float

tupla_4 = ('True', "False")  # tupla de string

tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7) ) # tupla mix
#Indices    0   1     2       3        4

print(type(tupla_1))
print(tupla_1)

print(type(tupla_2))
print(tupla_2)

print(type(tupla_3))
print(tupla_3)

print(type(tupla_4))
print(tupla_4)

print(type(tupla_5))
print(tupla_5)

#print("Elemenro posicion", tupla_5[2][0])

# Para obtener los elemntos de las tuplas vamos a utilizar sus indice
print("Elemenro posicion", tupla_5[2])

#Slicing de tuplas : Extraer subTuplas
print("Slicing")
print("Elemenro posicion", tupla_5[0:3])
print("Elemenro posicion", tupla_5[0:3][2])

#Inmutabilidad
#lista_total_1 = tupla_1 + tupla_2

#Artificios conversiones de lista a tuplas
lista_total = list(tupla_1) + list(tupla_2)
tupla_final = tuple(lista_total)
print(type(lista_total))

#Cambiar elementos
tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7) ) # tupla mix

print("Casi 1")
print(tupla_5[3][1])
tupla_5[3][1] = 22

#append() en tuplas  : Agregar elemtos a la tupla no se puede realizar por caracteristica de la inmutavilidad

#tupla_5.append("Python 3")
#print(tupla_5)

#Funciones de las tuplas : len(), index(), count()
tupla_5 = (1, 4.5, 'Hola', [1,2,3], (5,6,7), "Hola" ) # tupla 

print("La tupla tiene f len() :", len(tupla_5))  # Determina el numero de elemento de la tupla()

print("La tupla tiene f count() :", tupla_5.count('hola')) #Devuelve el numero de ocurrencias del dato enviado a la funcion count()

print("La tupla tiene f index() :", tupla_5.index('hola')) #Devuelve la posicio (indice) del elemento a buscar; la primera ocurrencia


# For : Iterar entre elementos y elemento
lista = [1,2,3,4,5,6,7,8,9]
#        0 1 2 .........

print("------------Estrutura While--------------")
indice = 0
while (indice < len(lista)):
    print(f"{indice} : {lista[indice]}")
    indice +=1
    
#Cambios para el estructura for
print("--------------Estrutura For---------------")
indice = 0
for dato in lista:
    print(f"{indice} : {dato}")
    indice += 1
    
#For se puede combinar con metodo llando : enumerate
print("--------------Estrutura For con metodo Enumerate---------------")

lista = [1,2,3,4,5,6,7,8,9]
#indice   0 1 2 .........

#(0,1)
#(1,2)
#(2,3)

for index,dato in enumerate(lista):
    print(f"{indice} : {dato}")
    
#For se puede combinar con metodo llando : range()

print("--------------Estrutura For con metodo range()---------------")
for dato in range(11):
    print(f" f1 {dato}")

for dato in range(1,11):
    print(f" f2 {dato}")
    
for dato in range(1,11,2):
    print(f" f3 {dato}")
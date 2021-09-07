#Paso por referencis : Se aplican directamente a las estructura como listas, tuplas, diccionario

def duplicar_numeros(numeros):
    if isinstance(numeros,tuple):
        temp_lista = list(numeros)
        for i,n in enumerate(temp_lista)
            temp_lista[i] *=2
        numeros = tuple(temp_lista)
        print(numeros)
        
numeros = (10,20,30,40)
print("lista Inicial", numeros)
duplicar_numeros(numeros)
# Estructura while

bandera = True
contador = 1

while contador <= 10:
    print(f" {contador} : Hola Mundo:")
    contador += 1
 
#while-else : continuo y break
print("while-Else")
contador = 1

while contador <= 5:
    print(f" {contador} : Hola Mundo:")
    contador += 1
else: 
    print("La estructura while se ejecuta correctamente!!!!")

# Break
print("-----------------while-break----------------")
contador = 1
while contador <= 4:
    print(f" {contador} : Hola Mundo:")
    if contador == 2:
        break
    contador += 1
else: 
    print("La estructura while se ejecuta correctamente!!!!")
    
# Continue
print("-----------------while-Continue----------------")
contador = 0

while contador <= 5:
    contador += 1
    if contador == 3 or contador == 4:
        continue
    print(f" {contador} : Hola mundo")    
else: 
    print("La estructura while se ejecuta correctamente!!!!")
    
    
    
    
# Estructura for

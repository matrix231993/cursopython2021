serie = int(input("ingreasr el limite de la serie \n"))
contador = 0

while contador < serie:
    contador +=1
    if not(contador % 2 == 0):
        continue
    contador +=1
    print(f"# {contador} :")
else:
    print(f"La serie de psres esta correcta")

print("Fin del programa")
    
    
    

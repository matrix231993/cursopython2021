#Definir cadenas o String ()
#

cadena_1 = "Mi pelicula favotita es :"   # Tipado dinamico  :
cadena_2 = "Avangers"

# Para contenar utilizamos signno "+"

cadena_3 = cadena_1 + " " +cadena_2

print(type(cadena_3))
print(cadena_3)

# Concatenar tambien vamos utiliza ","

cadena_1 = "Mi auto favorito es"
cadena_2 = "Mazda"
cadena_3 = "Toyota"

#Primera Forma
cadena_4 = cadena_1+cadena_2+cadena_3

#cadena_4 = cadena_1,cadena_2,cadena_3   

#print(type(cadena_4))
print("Primera Forma"+ ""+cadena_4)

#Segunda forma
#print(cadena_1,cadena_2,cadena_3)
suma = 5 + 5 + 300.2356565
print("El valor de la suma Forma2",round(suma,4))

#Tercera Forma
print(f"La cadena final es forma3: {suma}, {cadena_1} , {cadena_2}, {cadena_3}")

#Cuarta Forma
print("La cadena final es forma4 : {}, {}, {}, {}".format(suma,cadena_1,cadena_2,cadena_3))

#Print de caracteres especiales:  Se utiliza para dar formato a las cadenas o string
# \n , \r, \t
print("Se puede crear cadenas multineas\nutilizando secuencias de escapes.")

print("Menu Principarl 1.- Suma : 2.- Resta")

print(r"C:\Users\geovanny\nombre")      #raw

#Multilinea

print("""Una linea
segunda linea
tercera linea
cuarta linea""")

#Operacion multiplicacion (*)

cadena_1 = "*"
cadena_1 = "C:NombreCarpeta\n"

cadena_3 =  10  * "***\t"
print(cadena_3)

#Indeces en las cadenas

# "P  Y   T   H   O   N"
#  0  1   2   3   4   5       >>>>>>>>> Ascemdente
# -6  -5  -4  -3  -2  -1      >>>>>>>>> Descendente

CADENA= "PYTHON0"
print(CADENA[-1])
print(CADENA[-2])
print(CADENA[-3])
print(CADENA[-4])
print(CADENA[-5])
print(CADENA[-6])
print(CADENA[-7])






#Tercera Forma
#print("")




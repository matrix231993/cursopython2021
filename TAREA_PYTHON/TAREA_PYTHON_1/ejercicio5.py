

#EJERCICIO 6.- Calcular el área y el perímetro de un Rectángulo

#En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo, para ello deberemos crear las siguientes variables:

    #alto (int)

    #ancho (int)

#El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

    #Proporciona el alto:
    #Proporciona el ancho:
    #Area: <area>
    #Perímetro: <perimetro>

#Las fórmulas para calcular el área y el perímetro de un Rectángulo son:

#Área: alto * ancho





altura = int (input ('Ingresa la medida del altura: '))
ancho = int (input ('Ingresa la medida del ancho: '))

area=altura*ancho

perimetro=altura+ancho+altura+ancho

print(f"valor de la area {area}cm²")
print(f"valor del perimetro {perimetro}cm")
      
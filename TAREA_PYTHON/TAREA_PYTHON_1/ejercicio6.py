#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

#Por ejemplo: 1000 minutos son 16 horas y 40 minutos

valor = int(input("ingrese minuto para la convercion"))

hora = valor /60

minutos_restatante = hora % 60

print(f"hora : {hora}")
print(f"minutos_restatante : {minutos_restatante}")



#Parametros por defectos

def resta(a=None,b=None):
    
    if isinstance(a,int) and isinstance(b,int):
        resulatdo = a-b
    else:
        print("Error, no se puede realizar la operacion con dato que no sean Vase10")
        return
    return resulatdo

#Incovacion
r = resta(10,10)
print("El resultado es :", r)

#cadena = 10
#print(type(cadena) )
#resultado_validacion = isinstance(cadena, int)

#print(resultado_validacion)

a = '10a'
cadena_1 = None
for car in (list(a)):
    if isinstance(car,str):
        try:
            numerico = int(car)
        except:
            print("no pudo realizar el castin")
        finally:
            cadena_1 += numerico
            
def convertir():
    a = '10a'
    cadena_1 = ''
    lista_num = []
    
    for car in (list(a)):    # Lista ['1','0','a']
        if isinstance(car,str):
            try:
                print(type(car))
                numerico = int(car)
                lista_num.append(numerico)
            except:
                print("No pudo realizar el castin")
            
    print("Mi numero es ", str(lista_num))

convertir()
import math
#En este subprograma realizaremos la transformacion de un complejo escrito en
#forma polar a cartesiana
def polarACartesiano(m,a):
    print(a)
    return [math.degrees(math.cos(a)), math.sin(a)]
#En este subprograma realizaremos la transformacion de un complejo escrito en
#forma cartesiana a polar
def cartesianoAPolar(c1):
    #Definimos la parte reale e imaginaria

    r1 = c1[0]
    i1 = c1[1]

    return [round(modulo(c1), 2),round(math.degrees(math.atan(i1/r1)), 2)]
    
#En este subprograma realizaremos la impresion de un numero complejo en
#forma : a + b*i
def impresion(c1):
    #Definimos la parte reale e imaginaria

    r1 = c1[0]
    i1 = c1[1]

    #Revisaremos que signo tiene el numero imaginario para hacer correcta la
    #impresion
    
    if i1 > 0:
        print(str(r1)+" +"+str(i1)+"i")
        
    else:
        print(str(r1)+" "+str(i1)+"i")
#En este subprograma realizaremos el modulo de un numero complejo
def modulo(c1):
    #Definimos la parte real e imaginaria

    r1 = c1[0]
    i1 = c1[1]
    
    return round(((r1**2)+(i1**2))**(1/2), 2)

#En este subprograma realizaremos el conjugador de un numero complejo
def conjugado(c1):
    #Definimos la parte real e imaginaria

    r1 = c1[0]
    i1 = c1[1]

    return [r1,-i1]

#En este subprograma realizaremos la division de dos numeros complejos.
def division(c1, c2):
    #Definimos las partes reales de los nuemeros.

    r1 = c1[0]
    r2 = c2[0]

    #Definimos las partes imaginarias de los numeros.

    i1 = c1[1]
    i2 = c2[1]

    #Revisamos que no estemos dividiendo por cero (0).

    if r2 == 0 and i2 == 0:
        return None

    #Revisamos si alguna parte (la real o la imaginaria) del denominador es
    #cero (0), ya que si alguno lo es, esto nos facilita los calculos, de ser
    #asi retornamos la respuesta

    elif r2 == 0 and i2 != 0:
        
        r3 = i1/i2
        i3 = r1/i2
        return [r3, i3]

    elif r2 != 0 and i2 == 0:

        r3 = r1/r2
        i3 = i2/r2
        return [r3, i3]
    
    #Si ninguno es cero, multiplicamos al numerador y al denominador por la
    #conjugada del denominador, despues realizamos la division normal, ya que
    #estaremos dividiendo por un real
    
    else:
        z = conjugado(c2)
        numerador = producto(c1, z)
        denominador = producto(c2, z)
        return [round(numerador[0]/denominador[0],2),
                round(numerador[1]/denominador[0],2)]
        
        
#En este subprograma realizaremos el producto de dos numeros complejos.
def producto(c1, c2):
    #Definimos las partes reales de los nuemeros.

    r1 = c1[0]
    r2 = c2[0]

    #Definimos las partes imaginarias de los numeros.

    i1 = c1[1]
    i2 = c2[1]
    

    #Realizamos el producto de manera distributiva, guardaremos los resultados
    #teniendo en cuenta si son reales o imaginarios.

    r3 = r1 * r2
    r4 = i1 * i2
    
    i3 = r1 * i2
    i4 = i1 * r2

    #Multiplicamos r4 por (-1) ya que este resultado siempre nos dara un i**2

    r4 = r4 * (-1)

    #Retornamos el resultado, que es la suma de los resultados obtenidos en el
    #paso anterior.

    return [r3+r4, i3+i4]
    
#En este subprograma realizaremos la resta de dos numeros complejos.
def resta(c1, c2):
    #Definimos las partes reales de los nuemeros.

    r1 = c1[0]
    r2 = c2[0]

    #Definimos las partes imaginarias de los numeros.

    i1 = c1[1]
    i2 = c2[1]

    #Retornaremos la resta, restamos parte real con parte real y parte
    # imaginaria con parte imaginaria.

    return [r1-r2, i1-i2]


#En este subprograma realizaremos la suma de dos numeros complejos.
def suma(c1, c2):
    #Definimos las partes reales de los numeros.

    r1 = c1[0]
    r2 = c2[0]

    #Definimos las partes imaginarias de los numeros.

    i1 = c1[1]
    i2 = c2[1]

    #Retornamos la suma, sumamos parte real con parte real y pare imaginaria
    #con parte imaginaria.
    
    return [r1+r2, i1+i2]


#En el main del programa definimos los numeros complejos que utilizaremos
#y llamamos el metodo correspondiete a la operacion a ejecutar.
def main():
    
    complejo1 = [15,2]
    complejo2 = [3,2]
    modulo = 3.605551275463989 # 3+2i
    argumento = 33.690067525979785 # 3+2i
    # suma(complejo1, complejo2)
    # resta(complejo1, complejo2)
    # producto(complejo1, complejo2)
    # division(complejo1, complejo2)
    # conjugado (complejo1)
    # modulo(complejo1)
    # impresion(complejo2)
    # cartesianoAPolar(complejo2)
    print(polarACartesiano(modulo, argumento))
    
main()

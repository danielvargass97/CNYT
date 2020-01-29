import Numeros_complejos as NC
import copy
cont = 0
def Mandelbrot(z, c):
    global cont
    if NC.modulo(NC.suma((NC.potencia(z,2)),c)) > 2:
        cont += 1
        cont2 = copy.copy(cont)
        cont = 0
        #print("El numero "+str(c)+" no pertenece al conjunto de Mandelbrot")
        return False, cont2
    else:
        if cont > 30:
            cont = 0
            #print("El numero "+str(c)+" pertenece al conjunto de Mandelbrot")
            return True,0
        else:
            cont += 1
            return Mandelbrot(NC.suma((NC.potencia(z,2)),c),c)
        


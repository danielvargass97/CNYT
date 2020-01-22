import Numeros_complejos as NC

def test_suma():
    assert NC.suma([-3,2], [4,1]) == [1,3], 'Debe ser 1+3i'

def test_resta():
    assert NC.resta([-3,2], [4,1]) == [-7,1], 'Debe ser -7+i'

def test_producto():
    assert NC.producto([2,3], [0,4]) == [-12,8], 'Debe ser -12+8i'

def test_division():
    assert NC.division([5,7], [8,-9]) == [round((-23/145), 2),round((101/145), 2)], 'Debe ser'

def test_conjugado():
    assert NC.conjugado([10,10]) == [10,-10], 'Debe ser 10-10i'

if __name__ == '__main__':
    test_suma()
    test_resta()
    test_producto()
    test_division()
    test_conjugado()
    print('Prueba exitosa')

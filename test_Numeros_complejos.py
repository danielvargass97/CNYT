import Numeros_complejos as NC

def test_suma():
    assert NC.suma([-3,2], [4,1]) == [1,3], 'Debe ser 1+3i'

if __name__ == '__main__':
    test_suma()
    #test_resta()
    print('Prueba exitosa')
